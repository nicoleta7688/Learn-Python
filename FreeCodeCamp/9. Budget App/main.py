# Import math library
import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.get_balance() > amount:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for ledger in self.ledger:
            balance += ledger['amount']
        return balance

    def transfer(self, amount, category):
        if self.get_balance() >= amount:
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {category.name}'})
            category.ledger.append({'amount': amount, 'description': f'Transfer from {self.name}'})
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
    
    def __str__(self):
        balance = 0
        str_result = self.name.center(30, '*') #title
        # string.center(length, character)
        # length	    Required.   The length of the returned string
        # character	    Optional.   The character to fill the missing space on each side. Default is " " (space)
        str_result += '\n'

        for ledger in self.ledger:

            description_str = ledger['description'][:23]
            description_str = description_str.ljust(23)
    
            amount_str = f"{ledger['amount']:.2f}"
            amount_str = amount_str.rjust(7)

            str_result += f"{description_str}{amount_str}\n"
            balance += ledger['amount']

        str_result += f'Total: {balance}'
        return str_result

def create_spend_chart(categories):

    # calculate total spendings and spedings for each category
    chart_spendings = []
    total_spent = 0
    total_category_spent = 0
    for category in categories:
        for withdraw in category.ledger:
            if withdraw['amount'] < 0:
                total_category_spent += withdraw['amount'] * (-1)

        chart_spendings.append([category.name, total_category_spent])
        total_spent += total_category_spent
        total_category_spent = 0
    
    # calculate percentages for each category
    chart_percentages = []
    percentages = 0
    for chart_spent in chart_spendings:
            percentages = (chart_spent[1] * 100) / total_spent
            percentages = (math.floor(percentages/10)) * 10
            chart_percentages.append((chart_spent[0], percentages))
    # print(chart_percentages)

    str_chart = 'Percentage spent by category\n'

    # draw y-axis and labels 
    y_axis = ''
    for y_label in range(100, -1, -10):
        y_axis = f'{y_label}|'
        y_axis = y_axis.rjust(4)
 
        for percentage in chart_percentages:
            if y_label <= percentage[1]:
                y_axis += ' o '
            else:
                y_axis += '   '
        y_axis += ' \n'
        str_chart += y_axis

    nr_categories = len(chart_percentages)
    orizontal_line = '    '
    for n in enumerate(chart_percentages):
        orizontal_line += '---'
    orizontal_line += '-'
    str_chart += orizontal_line


    # find the maximum lenght of a category name
    max_category_len = 0
    for category_name in chart_percentages:
        if max_category_len < len(category_name[0]):
            max_category_len = len(category_name[0])

    # draw x_labels
    x_label = ''

    for index in range(0, max_category_len):
        # start the line with spaces:
        x_label += '\n     '
        
        for category_name in chart_percentages:
            # print(category_name[0])
            if len(category_name[0]) > index:
                x_label += f'{category_name[0][index]}  '
            else:
                x_label += '   ' # 3 spaces
        # end with end of line


    str_chart += x_label
    return str_chart


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
auto = Category('Auto')
food.transfer(100, clothing)
food.transfer(500, auto)

clothing.withdraw(99, 'groceries')
auto.deposit(1000, 'initial deposit')
auto.withdraw(700, 'groceries')

categories = [food, clothing, auto]
print(food)
print(create_spend_chart(categories))