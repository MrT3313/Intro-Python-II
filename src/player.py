# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curr_room='outside'):
        self.name = name
        self.curr_room = curr_room

    def move_player(self, command):
        print(f'MOVE THIS PLAYER: {command}')
    
    def __str__(self):
        output = ''
        output += f'PLAYER CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'Current Room: {self.curr_room}'

        return output

# Test Player Class
testPlayerClass = Player('testPlayer')
print(testPlayerClass)
