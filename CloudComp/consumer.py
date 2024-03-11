import pika
import pickle


creds = pika.PlainCredentials("user", "user")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=creds)
)
channel = connection.channel()

channel.queue_declare(queue="logs")

def callback(ch, method, properties, body):
    payload = pickle.loads(body)
    
    print(f"Received - {payload['number']}")

channel.basic_consume(queue="logs", on_message_callback=callback, auto_ack=True)

channel.start_consuming()