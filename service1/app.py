from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    service_name = os.environ.get('SERVICE_NAME', 'Service 1')
    return jsonify(message=f"Hello from {service_name}!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)