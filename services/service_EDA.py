import pika
import json
from flask import Flask

app = Flask(__name__)

def publish_event(event):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='events')
    channel.basic_publish(exchange='', routing_key='events', body=json.dumps(event))
    connection.close()

@app.route("/")
def home():
    publish_event({"source": "EDA", "event": "Service EDA foi chamado!"})
    return "Resposta do Serviço EDA"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004)    