from abc import ABC, abstractmethod

class Entry(ABC):
    def __init__(self, id, description, amount):
        self.id = id
        self.description = description
        self.amount = amount

    @abstractmethod
    def get_amount(self):
        pass


class IncomeEntry(Entry):
    def __init__(self, id, description, amount):
        super().__init__(id, description, amount)

    def get_amount(self):
        return self.amount

class ExpenseEntry(Entry):
    def __init__(self, id, description, amount):
        super().__init__(id, description, amount)

    def get_amount(self):
        return self.amount

class BudgetManager:
    def __init__(self, incomes, expenses):
        self.incomes = incomes
        self.expenses = expenses

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_income(self):
        return sum(income.amount for income in self.incomes)

    def get_total_expense(self):
        return sum(expense.amount for expense in self.expenses)

    def get_net_total(self):
        return self.get_total_income() - self.get_total_expense()