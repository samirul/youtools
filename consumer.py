import json
import os
import pika
import django
from pika.exceptions import AMQPConnectionError
from converter.binary_to_png import upload_image_from_byte_image_array

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtools.settings")
django.setup()
from images.models import Images

# RabbitMQ connection parameters
params = pika.URLParameters(os.environ.get('RABBITMQ_URL'))


def connect_consumer():
    # Establish connection
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='youtools-queue')

        def callback(ch, method, properties, body):
            try:
                print("message receiving....")
                if properties.type == 'created_new_image':
                    print("Task executing, please wait....")
                    data = body.decode('utf-8')
                    converted_data = json.loads(data)
                    spilt_name = str(converted_data['image_name']).split()
                    binary_to_image=upload_image_from_byte_image_array(byte_array=converted_data['image_data'], file_name=f"result_txt_2_img_{'_'.join(spilt_name)}.png")
                    
                    # Create the image record in the database
                    Images.objects.create(
                        id=converted_data['_id'],
                        image_data=binary_to_image,
                        image_name=converted_data['image_name']
                    )
                    print("Image created successfully")
            
            except Exception as e:
                # Log or handle errors during message processing
                print(f"Error processing message: {e}")

        # Start consuming messages from 'django_app' queue
        channel.basic_consume(queue='youtools_queue', on_message_callback=callback, auto_ack=True)
        print('Waiting for messages....')
        channel.start_consuming()

    except AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the channel and connection are closed if they were opened
        if 'channel' in locals() and channel.is_open:
            channel.close()
        if 'connection' in locals() and connection.is_open:
            connection.close()


if __name__ == '__main__':
    connect_consumer()