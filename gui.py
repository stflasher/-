import tkinter as tk
from tkinter import messagebox
from storage import DataStorage
from models import FinancialOperation

class FinancialPlannerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Financial Planner")
        self.master.geometry("400x300")
        self.storage = DataStorage()
        self.operations = self.storage.load_data()
        self.create_widgets()

    def create_widgets(self):
        self.amount_entry = tk.Entry(self.master, font=('Arial', 16))
        self.amount_entry.pack(pady=10, padx=10, ipadx=5, ipady=5)
        self.category_entry = tk.Entry(self.master, font=('Arial', 16))
        self.category_entry.pack(pady=10, padx=10, ipadx=5, ipady=5)
        self.date_entry = tk.Entry(self.master, font=('Arial', 16))
        self.date_entry.pack(pady=10, padx=10, ipadx=5, ipady=5)
        self.comment_entry = tk.Entry(self.master, font=('Arial', 16))
        self.comment_entry.pack(pady=10, padx=10, ipadx=5, ipady=5)
        self.add_button = tk.Button(self.master, text="Add Operation", command=self.add_operation)
        self.add_button.pack()

    def add_operation(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date = self.date_entry.get()
            comment = self.comment_entry.get()
            operation = FinancialOperation(amount, category, date, comment)
            self.operations.append(operation.__dict__)
            self.storage.save_data(self.operations)
            messagebox.showinfo("Success", "Operation added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter correct values.")
