import pika
import pickle


creds = pika.PlainCredentials("user", "user")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=creds)
)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")
q = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(q.method.queue, "logs")


def callback(ch, method, properties, body):
    payload = pickle.loads(body)
    print(f"Received - {payload}")

channel.basic_consume(queue=q.method.queue, on_message_callback=callback, auto_ack=True)

channel.start_consuming()