from flask import Flask, request, session, render_template, flash
from models import *

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

    income_amount = request.form["amount"]
    income_description = request.form["description"]

    error = False
    if not income_amount:
        flash("Please specify income amount")
        error = True
    else:
        try:
            income_amount = float(income_amount)
            if income_amount <= 0:
                flash("Please enter positive income")
                error = True
        except ValueError:
            flash("Please enter numerical income")
            error = True
    if not income_description:
        flash("Please enter income description")
        error = True
    if error:
        return render_template("index.html")

    INCOMES.append({"id" : len(INCOMES), "amount": income_amount, "description": income_description})
    return render_template("/index.html", income_amount=income_amount, income_description=income_description)


@app.route("/expense_submission", methods=["POST"])
def expense_submission():
    global EXPENSES

    expense_amount = request.form["amount"]
    expense_description = request.form["description"]

    error = False
    if not expense_amount:
        flash("Please specify expense amount")
        error = True
    else:
        try:
            expense_amount = float(expense_amount)
            if expense_amount <= 0:
                flash("Please enter positive expense")
                error = True
        except ValueError:
            flash("Please enter numerical expense")
            error = True
    if not expense_description:
        flash("Please enter expense description")
        error = True
    if error:
        return render_template("index.html")

    EXPENSES.append({"id": len(EXPENSES), "amount": expense_amount, "description": expense_description})
    return render_template("/index.html", expense_amount=expense_amount, expense_description=expense_description)


@app.route("/summary")
def summary():
    global INCOMES, EXPENSES

    if not INCOMES and not EXPENSES:
        return render_template("index.html")
    return render_template("summary.html", budgets=INCOMES, expenses=EXPENSES)


@app.route("/reset")
def reset():
    session.clear()
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)