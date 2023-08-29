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
        # elif command == "b":
        #     self.move_backward()
        # elif command == "l":
        #     self.turn_left()
        # elif command == "r":
        #     self.turn_right()
        # elif command == "u":
        #     self.turn_up()
        # elif command == "d":
        #     self.turn_down()

    def get_position(self):
        return self.x, self.y, self.z

    def get_direction(self):
        return self.direction

if __name__ == "__main__":
    
    chandrayaan = chanda(0, 0, 0, "N")
    commands = ["f", "r", "f", "u", "b", "l"]
    for command in commands:
        chandrayaan.execute_command(command)
    print("Final Position:", chandrayaan.get_position())
    print("Final Direction:", chandrayaan.get_direction())
