def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'],expenses))

def filter_expenses_by_category(expenses, category):
    pass
    
test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8])))
print(sum(map(test, [2, 3, 5, 8])))

expenses = []