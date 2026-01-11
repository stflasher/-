class FinancialOperation:
    def __init__(self, amount, category, date, comment):
        self.amount = amount
        self.category = category
        self.date = date
        self.comment = comment

class Category:
    def __init__(self, name):
        self.name = name
