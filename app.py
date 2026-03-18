from flask import Flask, jsonify, request, session, render_template

app = Flask(__name__)
app.secret_key = "secretkey123"

INCOMES = []
EXPENSES = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/income_submission", methods=["POST"])
def income_submission():
    global INCOMES

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    try:
        income_amount = int(data.get("amount"))
    except ValueError:
        return jsonify({"error": "Non-Numerical Amount"}), 400
    income_description = data.get("description")
    INCOMES += {"id" : len(INCOMES), "income": income_amount, "description": income_description}

    return render_template("/index.html", income_amount=income_amount, income_description=income_description)


@app.route("/expense_submission", methods=["POST"])
def expense_submission():
    global EXPENSES

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    try:
        expense_amount = int(data.get("amount"))
    except ValueError:
        return jsonify({"error": "Non-Numerical Amount"}), 400
    expense_description = data.get("description")
    EXPENSES += {"id": len(EXPENSES), "income": expense_amount, "description": expense_description}

    return render_template("/index.html", expense_amount=expense_amount, expense_description=expense_description)


@app.route("/summary")
def summary():
    global INCOMES, EXPENSES

    if not INCOMES and not EXPENSES:
        return render_template("index.html")
    return render_template("summary.html")


@app.route("/reset")
def reset():
    session.clear()
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)