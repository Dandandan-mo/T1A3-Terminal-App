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

class Category:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    def withdraw(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})

    # def display(self):
    #     print(self.details)


