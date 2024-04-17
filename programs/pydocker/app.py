from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)