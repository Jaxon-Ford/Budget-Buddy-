from abc import ABC, abstractmethod

class Entry(ABC):
    def __init__(self,description,amount):
        self.description = description
        self.amount = amount
        None

    @abstractmethod
    def get_amount(self):
        pass

def Income_Entry(Entry):
    def __init__(self, description, amount):
     super().__init__(description, amount)

    def get_amount(self):
        return self.amount

def Expense_Entry(Entry):
    def __init__(self,description, amount):
        super().__init__(description, amount)

def get_expense(self):
    return self.amount