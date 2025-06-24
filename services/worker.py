import pika
import json

def callback(ch, method, properties, body):
    event = json.loads(body)
    print(f"📥 Evento recebido: {event}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='events')
channel.basic_consume(queue='events', on_message_callback=callback, auto_ack=True)

print("🎧 Aguardando eventos...")
channel.start_consuming()