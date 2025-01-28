"""
    Sending data to sentiment analysis flask app using RabbitMq.
"""

import os
import ssl
import json
import logging
import pika
from pika.exceptions import ConnectionClosedByBroker, AMQPConnectionError

class RabbitMQConnection:
    """Sending event-driven data to sentiment analysis flask app."""
    def __init__(self):
        """Required parameters"""
        self.rabbitmq_url = os.environ.get('RABBITMQ_URL')

    def connect(self):
        """For Connecting to RabbitMQ server and channel.

        Returns:
            return: channel for make connections.
        """
        params = pika.URLParameters(self.rabbitmq_url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        return channel
    
    def publish_sentiment_analysis(self, method, body):
        """publish is responsible to send data to specific routing
           key that has been defined in routing key.

        Args:
            method (string): Send custom string for identifying data by consumer.
            body (json): Sending json type body data to consumer.
        """
        channel = self.connect()
        properies = pika.BasicProperties(type=method)

        try:
            channel.basic_publish(
                exchange='',
                routing_key='sent_user_data-queue_sentiment_analysis_flask',
                body= json.dumps(body),
                properties=properies
            )
            print("Message published successfully.")

        except (ConnectionClosedByBroker, AMQPConnectionError, ssl.SSLEOFError) as err:
            logging.error('Could not publish message to RabbitMQ: %s', err)
            # Reconnect to RabbitMQ.
            channel = self.connect()
        except pika.exceptions.AMQPError as err:
            # Handle errors in publishing messages.
            print(f"Failed to publish message: {err}.")
    
