from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def random_number():
    service_name = os.environ.get('SERVICE_NAME', 'Service 3')
    number = random.randint(1, 100)
    return jsonify(message=f"Hello from {service_name}! Here's a random number: {number}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)