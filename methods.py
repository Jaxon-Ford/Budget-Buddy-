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
        session["incomes"] = []


def load_expenses_into_session():
        session["expenses"] = []

def load_incomes():
    return [IncomeEntry(i["id"], i["description"], i["amount"]) for i in session.get("incomes", [])]

def load_expenses():
    return [ExpenseEntry(i["id"], i["description"], i["amount"]) for i in session.get("expenses", [])]
