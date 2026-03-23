from models import *
from flask import session

def init_session():
    if "incomes" not in session:
        session["incomes"] = []
    if "expenses" not in session:
        session["expenses"] = []


def load_incomes(income_session):
    print("Income session: ", income_session)
    incomes = []
    for i in income_session:
        incomes.append(IncomeEntry(i["id"], i["description"], i["amount"]))

    return incomes


def load_expenses(expense_session):
    expenses = []
    for e in expense_session:
        expenses.append(ExpenseEntry(e["id"], e["description"], e["amount"]))

    return expenses