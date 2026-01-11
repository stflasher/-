import csv
import json
import os

class DataStorage:
    def __init__(self, filename='data/financial_data.csv'):
        self.filename = filename

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return list(csv.DictReader(file))

    def save_data(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
