import unittest
from models import FinancialOperation
from analysis import FinancialAnalyzer

class TestFinancialOperation(unittest.TestCase):
    def test_operation_creation(self):
        operation = FinancialOperation(100, 'Food', '2023-01-01', 'Grocery shopping')
        self.assertEqual(operation.amount, 100)
        self.assertEqual(operation.category, 'Food')

class TestFinancialAnalyzer(unittest.TestCase):
    def test_total_by_category(self):
        operations = [
            {'amount': 100, 'category': 'Food'},
            {'amount': 50, 'category': 'Food'},
            {'amount': 200, 'category': 'Transport'}
        ]
        analyzer = FinancialAnalyzer(operations)
        result = analyzer.total_by_category()
        self.assertEqual(result['Food'], 150)
        self.assertEqual(result['Transport'], 200)

if __name__ == '__main__':
    unittest.main()
