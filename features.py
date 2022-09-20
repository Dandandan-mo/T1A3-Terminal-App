details = []
class TotalBalance:
    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        title = "_"*26 + "Summary" + "_"*26 + "\n"
        items = ""
        total = 0
        for item in details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"

            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

class Income:
    def __init__(self, c_category, c_description, c_amount):
        self.category = c_category
        self.description = c_description
        self.amount = c_amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    # def display(self):
    #     print(self.details)


class Expense:
    def __init__(self, d_category, d_description, d_amount):
        self.category = d_category
        self.description = d_description
        self.amount = d_amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})

    # def display(self):
    #     print(self.details)

