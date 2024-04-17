from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/produce', methods=['POST'])
def produce_message():
    message = request.json['message']
    print("Hello world")
    producer.send('test_topic', value=message.encode())
    return jsonify({'status': 'success'})

@app.route('/consume', methods=['GET'])
def consume_message():
    consumer = KafkaConsumer('test_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    messages = [message.value.decode() for message in consumer]
    consumer.close()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
