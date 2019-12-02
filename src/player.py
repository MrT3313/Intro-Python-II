# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
        self.backpack = []

    def move_player(self, command):
        print(f'MOVE THIS PLAYER: {command}')
        print(f'Testing command formation => {command}_to')

        if getattr(self.curr_room, f'{command}_to') is not None:
            self.curr_room = getattr(self.curr_room, f'{command}_to')
        else:
            print(f'!! -- Direction not available from your current room -- !!')

    def __str__(self):
        output = '*\n'
        output += f'PLAYER CLASS \n'
        output += f'Name: {self.name} \n'
        output += f'**\n'
        output += f'Current Room:\n'
        output += f'{self.curr_room}\n'
        output += f'**\n'
        output += '*'

        return output

# Test Player Class
# testPlayerClass = Player('testPlayer')
# print(testPlayerClass)
