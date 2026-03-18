from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = "secretkey123"

@app.route("/", METHODS=["POST"])
def home():
    None

@app.route("/summary")
def summary():
    None

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)