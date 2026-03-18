from flask import Flask, jsonify, request

app = Flask(__name__)

app.route("/")
def home():
    None

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)