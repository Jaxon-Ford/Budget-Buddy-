from abc import ABC, abstractmethod

class Entry(ABC):
    def __init__(self, id, description, amount):
        self.id = id
        self.description = description
        self.amount = amount

    @abstractmethod
    def get_amount(self):
        pass


class Income_Entry(Entry):
    def __init__(self, id, description, amount):
        super().__init__(id, description, amount)


class Expense_Entry(Entry):
    def __init__(self, id, description, amount):
        super().__init__(id, description, amount)

class BudgetManager():
    def __init__(self, incomes, expenses):
        self.incomes = incomes
        self.expenses = expenses

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_income(self):
        total_income = 0
        for income in self.incomes:
            total_income += income
        return total_income

    def get_total_expense(self):
        total_expense = 0
        for expense in self.expenses:
            total_expense += expense
        return total_expense

    def get_net_total(self):
        return self.get_total_income() - self.get_total_expense()