from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total requests', ['endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])


@app.route('/api/health')                                                                                                                                  
def health():
    REQUEST_COUNT.labels(endpoint='/api/health').inc()
    with REQUEST_LATENCY.labels(endpoint='/api/health').time():
        return jsonify({"status": "ok", "service": "backend"})                                                                                             

                                                                                                                                                            
@app.route('/api/hello')
def hello():
    REQUEST_COUNT.labels(endpoint='/api/hello').inc()
    with REQUEST_LATENCY.labels(endpoint='/api/hello').time():
        return jsonify({"message": "Hello from Backend!"})


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
