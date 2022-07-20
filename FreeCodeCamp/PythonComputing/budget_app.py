from itertools import zip_longest


class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __repr__(self):

        # first line of output string is the title with the category centered
        output = f"{str(self.category).center(30, '*')}\n"

        for record in self.ledger:
            description = record['description'][:23]
            amount = f"{record['amount']:.2f}"[-7:]
            output += f"{description}{amount.rjust(30-len(description))}\n"

        # total for the category is the last line to copy to the output string
        output += f"Total: {self.get_balance():.2f}"

        return output

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': float(amount), 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': 0-float(amount), 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        amount = float(amount)
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        if float(amount) > self.get_balance():
            return False
        return True


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)


def extract_percents(categories):
    total_withdrawals = 0
    category_withdrawals = []

    # total withdrawals and category withdrawals determined in these loops
    for cat in categories:
        cw = 0
        for ledger in cat.ledger:
            if ledger['amount'] < 0:
                total_withdrawals += ledger['amount'] * -1
                cw += ledger['amount'] * -1
        category_withdrawals.append(cw)

    category_spending = [int((i / total_withdrawals) * 100) for i in category_withdrawals]
    prcnt_rnd_dwn = [i - (i % 10) for i in category_spending]

    return prcnt_rnd_dwn


def create_spend_chart(categories):

    cp = extract_percents(categories)
    catg_chars = []
    output_str = 'Percentage spent by category\n'

    cat_fill_width = 0

    if len(categories) == 1:
        cat_fill_width = 4
    elif len(categories) == 2:
        cat_fill_width = 7
    elif len(categories) == 3:
        cat_fill_width = 10
    elif len(categories) == 4:
        cat_fill_width = 13

    for i in range(100, -1, -10):
        output_str += f'{i}'.rjust(3) + '|'
        output_str += ' '
        for c in cp:
            if i <= c:
                output_str += 'o  '
            else:
                output_str += '   '
        output_str += '\n'
    output_str += '    ' + ''.ljust(cat_fill_width, '-') + '\n'

    for c in categories:
        cat_split = []
        for char in c.category:
            cat_split.append(char)
        catg_chars.append(cat_split)

    for vals in zip_longest(*catg_chars, fillvalue=' '):
        output_str += '   '
        for i in vals:
            output_str += '  ' + i
        output_str += '  \n'

    output_str = output_str.rstrip()

    return output_str+'  '


print(create_spend_chart([food, clothing, auto]))
