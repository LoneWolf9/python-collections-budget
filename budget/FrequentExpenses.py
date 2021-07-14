from . import Export
from collections.abc import collections


expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
