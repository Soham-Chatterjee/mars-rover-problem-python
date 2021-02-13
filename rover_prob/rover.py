from .position import position

class rover(object):
    available_commands = {
        "M": 'move',
        "L": 'turn_left',
        "R": 'turn_right'
    }

    directions = {
        "N" : 1,
        "E" : 2,
        "S" : 3,
        "W" : 4
    }

    head = directions["N"]

    def __init__(self, plateau, position, head):
        self.plateau = plateau
        self.position = position
        self.head = head

    def __str__(self):
        return self.curpos

    def setpos(self, x, y, head):
        if not isinstance(self.position, position):
            self.position = position(x,y)
        else:
            self.position.x = x
            self.position.y = y
        self.head = head

    @property
    def curpos(self):
        return f'{self.position.x} {self.position.y} {self.get_head}'

    @property
    def get_head(self):
        directions = list(self.directions.keys())

        try:
            direction = directions[self.head - 1]
        except IndexError:
            direction = 'N'
            print("Wrong direction!")
        
        return direction

    def functioning(self, commands):
        for i in range(len(commands)):
            self.run_command(commands[i])

    def run_command(self, command):
        if "L" == command:
            self.turn_left()
        elif "R" == command:
            self.turn_right()
        elif "M" == command:
            if not self.move():
                print("No coordinate beyond this")
        else:
            print("Wrong command!")

    def move(self):
        if not self.plateau.isavailable_move(self.position):
            return False
        if self.directions['N'] == self.head:
            self.position.y += 1
        elif self.directions['E'] == self.head:
            self.position.x += 1
        elif self.directions['S'] == self.head:
            self.position.y -= 1
        elif self.directions['W'] == self.head:
            self.position.x -= 1

        return True

    def turn_left(self):
        if (self.head - 1) < self.directions['N']:
            self.head = self.directions['W']
        else:
            self.head -= 1
    
    def turn_right(self):
        if (self.head + 1) > self.directions['W']:
            self.head = self.directions['N']
        else:
            self.head += 1