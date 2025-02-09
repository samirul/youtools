"""
    This RabbitMQ Consumer is a subscriber from the publisher
    text2image flask app. Data will come from the text2image
    flask app through the RabbitMQ Queue(FIFO) and will interact with django.  
"""

import sys
import json
import os
import pika
import django
from pika.exceptions import AMQPConnectionError


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtools.settings")
django.setup()
# Importing django models after django setup so we
# can access django models properly outside django projects. 
from images.models import Images
from accounts.models import User
from converter.binary_to_png import upload_image_from_byte_image_array
from delete_images.delete import delete_data_from_media_container

# RabbitMQ connection parameters.
params = pika.URLParameters(os.environ.get('RABBITMQ_URL'))


def connect_consumer():
    """For connecting and waiting to get messages from the producer."""
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='youtools-queue_text2image')

        def callback(ch, method, properties, body):
            """Responsible for getting properties type and
                json data from producer and execute it in current consumer. 

            Args:
                ch (Parameter): Not used but needed.
                method (Parameter): Not used but needed.
                properties (Parameter): for getting properties type so can execute.
                specific task needed from producer to consumer.
                body (Parameter): json data from the producer.
            """
            try:
                print("message receiving....")
                if properties.type == 'created_new_image':
                    print("Task executing, please wait....")
                    data = body.decode('utf-8')
                    converted_data = json.loads(data)
                    spilt_name = str(converted_data['image_name']).split()
                    binary_to_image=upload_image_from_byte_image_array(byte_array=converted_data['image_data'], file_name=f"result_txt_2_img_{'_'.join(spilt_name)}.png")
                    user = User.objects.get(id=converted_data['user_id'])
                    
                    # Create the image record in the database.
                    Images.objects.create(
                        id=converted_data['_id'],
                        image_data=binary_to_image,
                        image_name=converted_data['image_name'],
                        user=user
                    )
                    print("Image uploaded successfully")

                if properties.type == 'image_data_Delete_from_flask':
                    # deleting image data from the database.
                    print("Task executing, please wait....")
                    ids = body.decode('utf-8')
                    converted_id = json.loads(ids)
                    try:
                        image = Images.objects.filter(id=converted_id).first()
                        if image:
                            image_name = str(image.image_name).split()
                            image_name_joined = "_".join(image_name)
                            delete_data_from_media_container(f"/vol/web/media/images/result_txt_2_img_{image_name_joined}.png")
                            image.delete()
                            print("Image deleted successfully")
                        else:
                            print(f"Image with {converted_id} not found")
                    except Exception as e:
                        print(f"Something is wrong: {e}")
                    
            
            except Exception as e:
                # Log or handle errors during message processing.
                print(f"Error processing message: {e}")

        # Start consuming messages from 'youtools-queue_text2image' queue.
        channel.basic_consume(queue='youtools-queue_text2image', on_message_callback=callback, auto_ack=True)
        print('Waiting for messages....')
        channel.start_consuming()

    except AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the channel and connection are closed if they were opened.
        if 'channel' in locals() and channel.is_open:
            channel.close()
        if 'connection' in locals() and connection.is_open:
            connection.close()


if __name__ == '__main__':
    connect_consumer()