# app.py
from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka-service:9092')
consumer = KafkaConsumer('test-topic', bootstrap_servers='kafka-service:9092')

@app.route('/endpoint1', methods=['POST'])
def endpoint1():
    data = request.get_json()
    producer.send('test-topic', value=data)
    return jsonify({"message": "Data sent to Kafka"})

@app.route('/endpoint2', methods=['GET'])
def endpoint2():
    message = next(consumer)
    return jsonify({"data": message.value.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)