import pandas as pd

class FinancialAnalyzer:
    def __init__(self, operations):
        self.operations = pd.DataFrame(operations)

    def total_by_category(self):
        return self.operations.groupby('category')['amount'].sum()

    def total_income_expense(self):
        return self.operations['amount'].sum()
