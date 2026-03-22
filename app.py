from flask import Flask, request, render_template, flash, redirect, url_for
from methods import *

app = Flask(__name__)
app.secret_key = "secretkey123"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/income_submission", methods=["POST", "GET"])
def income_submission():
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

    session["incomes"].append({
        "id": len(session["incomes"]),
        "amount": income_amount,
        "description": income_description
    })

    print(session["incomes"])
    return redirect(url_for("home"))


@app.route("/expense_submission", methods=["POST", "GET"])
def expense_submission():
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

    session["expenses"].append({
        "id": len(session["expenses"]),
        "amount": expense_amount,
        "description": expense_description
    })

    print(session["expenses"])
    return redirect(url_for("home"))


@app.route("/summary")
def summary():
    incomes = load_incomes()
    expenses = load_expenses()
    manager = BudgetManager(incomes, expenses)

    print(session["incomes"])
    print(session["expenses"])


    return render_template("summary.html", incomes=incomes, expenses=expenses, manager=manager)


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
    init_session()