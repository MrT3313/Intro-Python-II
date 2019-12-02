
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def __str__(self):
        output = ''
        output += f'ITEM CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Description: {self.desc}'

        return output

# Test Item Class
# testItemClass = Item('testItem', 'testItem description')
# print(testItemClass)

class Money(Item):
    def __init__(self, name, desc, amount, denomination):
        super().__init__(name, desc)
        self.amount = amount
        self.denomination = denomination

    def __str__(self):
        output = f''
        output += f'MONEY CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Description: {self.desc} \n'
        output += f'Amount: {self.amount} \n'
        output += f'Denomination: {self.denomination} \n'

        return output

class Food(Item):
    def __init__(self, name, desc, weight, value):
        super().__init__(name, desc)
        self.weight = weight
        self.value = value

    def __str__(self):
        output = f''
        output += f'FOOD CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Description: {self.desc} \n'
        output += f'Weight: {self.weight} \n'
        output += f'Value: {self.value} \n'

        return output