from flask import Flask,jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def hello():
    #return "<h1>Hello, World!</h1>"
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')
def health_check():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

