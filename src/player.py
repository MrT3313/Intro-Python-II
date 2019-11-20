# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
    
    def __str__(self):
        output = ''
        output += f'PLAYER CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Current Room: {self.curr_room}'

        return output

# Test Player Class
testPlayerClass = Player('testPlayer', 'outside')
print(testPlayerClass)
