from flask import session
from models import *

def init_session():
    if "incomes" not in session:
        session["incomes"] = []
    if "expenses" not in session:
        session["expenses"] = []

def load_incomes():
    return [IncomeEntry(i["id"], i["description"], i["amount"]) for i in session.get("incomes", [])]

def load_expenses():
    return [ExpenseEntry(i["id"], i["description"], i["amount"]) for i in session.get("expenses", [])]
