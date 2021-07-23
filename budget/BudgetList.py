class BudgetList:

    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if (self.sum_expenses & & item > self.budget):
            append(self.expenses[item])
            self.expenses += item
        else:
            append(self.overages[item])
            self.sum_overages += item

    def __len__(self):
