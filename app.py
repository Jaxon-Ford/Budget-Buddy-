from flask import Flask, jsonify, request, session, render_template

app = Flask(__name__)
app.secret_key = "super duper secret key"

@app.route("/", methods=["POST"])
def home():
    None

@app.route("/summary")
def summary():
    None


def clear():
    session.clear()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)