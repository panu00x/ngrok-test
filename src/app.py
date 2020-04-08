from flask import Flask
APP = Flask(__name__)
PORT = 5000


@APP.route('/ngrok')
def hello_world():
    return 'Hello, Ngrok!'


if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=PORT)
