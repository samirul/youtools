"""
    This RabbitMQ Consumer is a subscriber from the publisher
    Sentiment-Analysis flask app. Data will come from the Sentiment-Analysis
    flask app through the RabbitMQ Queue(FIFO) and will interact with django.  
"""

import json
import os
import sys
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
from sentiment_analysis.models import SentiMentAnalysis, Category
from accounts.models import User

class RabbitMQConsumer:
    """Created the class for getting messages from the RabbitMQ Queue."""
    def __init__(self):
        self.rabbitmq_url = os.environ.get('RABBITMQ_URL')

    def connect_consumer(self):
        """For connecting and waiting to get messages from the producer."""
        try:
            params = pika.URLParameters(self.rabbitmq_url)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            channel.queue_declare(queue='youtools-queue_sentiment_analysis')

            def callback(ch, method, properties, body):
                """Responsible for getting properties type and
                   json data from producer and execute it in current consumer. 

                Args:
                    ch (Parameter): Not used but needed.
                    method (Parameter): Not used but needed.
                    properties (Parameter): for getting properties type so can execute
                    specific task needed from producer to consumer.
                    body (Parameter): json data from the producer.
                """
                try:
                    print("message receiving....")
                    if properties.type == 'task_category_saved':
                        # saving new category in the database.
                        print("Task executing, please wait....")
                        data = body.decode('utf-8')
                        converted_data = json.loads(data)
                        category = Category.objects.select_related('user').filter(id=converted_data['_id']).first()
                        user = User.objects.get(id=converted_data['user'])
                        if not category:
                            Category.objects.create(
                                id = converted_data['_id'],
                                category_name = converted_data['category_name'],
                                user = user
                            )
                        print("Data from sentiment-Analysis category flask saved Successfully.")

                    if properties.type == 'task_data_saved':
                        # saving new sentiment analysis in the database.
                        print("Task executing, please wait....")
                        data = body.decode('utf-8')
                        converted_data = json.loads(data)
                        user = User.objects.get(id=converted_data['user'])
                        category = Category.objects.get(id=converted_data['category'])
                        SentiMentAnalysis.objects.create(
                            id = converted_data['_id'],
                            video_title = converted_data['video_title'],
                            video_url = converted_data['video_url'],
                            comment = converted_data['comment'],
                            main_result = converted_data['main_result'],
                            other_result = converted_data['other_result'],
                            user = user,
                            category=category
                        )
                        print("Data from sentiment-Analysis flask saved Successfully.")

                    if properties.type == 'delete_data_from_youtools_django':
                        # deleting sentiment analysis data from the database.
                        data = body.decode('utf-8')
                        converted_data = json.loads(data)
                        try:
                            sentiment_analysis = SentiMentAnalysis.objects.select_related('user').filter(id=converted_data).first()
                            if sentiment_analysis:
                                sentiment_analysis.delete()
                            print("Data from sentiment-Analysis deleted successfully.")
                        except Exception as e:
                            print(e)
                            print("Data from sentiment-Analysis failed to delete.")

                    if properties.type == 'delete_data_and_category_from_django_category':
                        # deleting category and sentiment analysis data from the database.
                        data = body.decode('utf-8')
                        converted_data = json.loads(data)
                        try:
                            category = Category.objects.select_related('user').filter(id=converted_data).first()
                            sentiment_analysis = SentiMentAnalysis.objects.select_related('user').filter(category=category.id)
                            if category:
                                category.delete()
                                sentiment_analysis.delete()
                            print("Data from category and sentiment-Analysis deleted successfully.")
                        except Exception as e:
                            print(e)
                            print("Data from category and sentiment-Analysis failed to delete.")
                    
                except Exception as e:
                        # Log or handle errors during message processing.
                        print(f"Error processing message: {e}.")
                # Start consuming messages from 'youtools-queue_sentiment_analysis' queue.
            channel.basic_consume(queue='youtools-queue_sentiment_analysis', on_message_callback=callback, auto_ack=True)
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
    rabbitmq_consumer = RabbitMQConsumer()
    rabbitmq_consumer.connect_consumer()