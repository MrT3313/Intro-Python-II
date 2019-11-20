
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def __str__(self):
        output = ''
        output += f'ITEM CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Description: {self.desc} \n'

        return output

# Test Item Class
testItemClass = Item('testItem', 'testItem description')
print(testItemClass)