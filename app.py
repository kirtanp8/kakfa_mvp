from flask import Flask
from kafka import KafkaProducer

app = Flask(__name__)

@app.route('/')
def index():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('test-topic', b'Hello, Kafka!')
    print("Message sent to Kafka topic: test-topic") 
    return 'Message sent to Kafka topic: test-topic'

if __name__ == '__main__':
    app.run(debug=True)
