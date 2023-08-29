# constants for direction
NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
UP = "U"
DOWN = "D"
class chanda:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def execute_command(self, command):
        if command == "f":
            self.move_forward()
        elif command == "b":
            self.move_backward()
        elif command == "l":
            self.turn_left()
        elif command == "r":
            self.turn_right()
        # elif command == "u":
        #     self.turn_up()
        # elif command == "d":
        #     self.turn_down()

    
    def move_forward(self):
        if self.direction =="N":
            self.y += 1
        elif self.direction =="S":
            self.y -= 1
        elif self.direction =="E":
            self.x += 1
        elif self.direction =="W":
            self.x -= 1
        elif self.direction == 'U':
            self.z += 1
        elif self.direction == 'D':
            self.z -= 1
    def move_backward(self):
        if self.direction =="N":
            self.y -= 1
        elif self.direction =="S":
            self.y += 1
        elif self.direction =="E":
            self.x -= 1
        elif self.direction =="W":
            self.x += 1
        elif self.direction =="U":
            self.z -= 1
        elif self.direction =="D":
            self.z += 1
    def turn_left(self):
        rotation_mapping = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N",
            "U": "D",
            "D": "U"
        }
        self.direction = rotation_mapping[self.direction]

    def turn_right(self):
        rotation_mapping = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N",
            "U": "D",
            "D": "U"
        }
        self.direction = rotation_mapping[self.direction]
    def get_position(self):
        return self.x, self.y, self.z

    def get_direction(self):
        return self.direction

if __name__ == "__main__":
    
    chandrayaan = chanda(0, 0, 0, "N")
    commands = ["f", "r", "u", "b", "l"]
    for command in commands:
        chandrayaan.execute_command(command)
    print("Final Position:", chandrayaan.get_position())
    print("Final Direction:", chandrayaan.get_direction())
