from flask import session
from models import *
import os
import json

INCOME_FILE = "data/incomes.json"
EXPENSE_FILE = "data/expenses.json"

def init_session():
    if "incomes" not in session:
        load_incomes_into_session()

    if "expenses" not in session:
        load_expenses_into_session()

def load_incomes_into_session():
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r") as f:
            session["incomes"] = json.load(f)
    else:
        session["incomes"] = []


def load_expenses_into_session():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            session["expenses"] = json.load(f)
    else:
        session["expenses"] = []

def save_incomes():
    with open(INCOME_FILE, "w") as f:
        json.dump(session["incomes"], f)

def save_expenses():
    with open(EXPENSE_FILE, "w") as f:
        json.dump(session["expenses"], f)

def load_incomes():
    return [IncomeEntry(i["id"], i["description"], i["amount"]) for i in session.get("incomes", [])]

def load_expenses():
    return [ExpenseEntry(i["id"], i["description"], i["amount"]) for i in session.get("expenses", [])]
