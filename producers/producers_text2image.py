"""
    Sending data to text2image flask app using RabbitMQ.
"""

import os
import ssl
import json
import logging
import pika
from pika.exceptions import ConnectionClosedByBroker, AMQPConnectionError

# RabbitMQ connection parameters/URLS
def connecting_rabbitmq():
    """For connecting to rabbitMQ server.

    Returns:
        Return: Connection channel after connecting to the rabbitMQ server.
    """
    params = pika.URLParameters(os.environ.get('RABBITMQ_URL')) 
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    return channel

def publish_text2_image(method, body):
    """publish is responsible to send data to specific routing
       key that has been defined in routing key.

    Args:
        method (string): Send custom string for identifying data by consumer.
        body (json): Sending json type body data to consumer.
    """
    channel = connecting_rabbitmq()
    properties = pika.BasicProperties(type=method)

    try:
        # Publish the message to the 'send_data_text2image' queue.
        channel.basic_publish(
            exchange='',
            routing_key='send_data_text2image',
            body=json.dumps(body), 
            properties=properties 
        )
        print("Message published successfully")
    except (ConnectionClosedByBroker, AMQPConnectionError, ssl.SSLEOFError) as err:
            logging.error('Could not publish message to RabbitMQ: %s', err)
            # Reconnect to RabbitMQ.
            channel = connecting_rabbitmq()
    except pika.exceptions.AMQPError as err:
        # Handle errors in publishing messages.
        print(f"Failed to publish message: {err}")