import pika
import pickle

creds = pika.PlainCredentials("user", "user")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=creds)
)
channel = connection.channel()

channel.queue_declare(queue="logs")

for i in range(50):
    payload = {
        "name": "test",
        "age": 12,
        "number":i
    }

    channel.basic_publish(exchange='', routing_key="logs", body=pickle.dumps(payload))

connection.close()