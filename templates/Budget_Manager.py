from flask import Flask
from templates.Entry import Expense_Entry


class Budget_Manager():

  def get_incomes(self,incomes,expenses):
     add_income = incomes,
     add_expenses = expenses,
     get_total_income = add_income + add_expenses,
     get_total_expenses = add_expenses + expenses,
     get_net_total = get_total_income + get_total_expenses

     return get_net_total
