from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def time():
    service_name = os.environ.get('SERVICE_NAME', 'Service 2')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(message=f"Hello from {service_name}! The current time is: {current_time}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)