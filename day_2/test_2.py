FILE = "data.txt"
FORWARD = "forward"
DOWN = "down"
UP = "up"


class Submarine:
    def __init__(self, depth=0, horizontal_position=0, aim=0):
        self.depth = depth
        self.horizontal_position = horizontal_position
        self.aim = aim

    def update_aim_down(self, aim):
        self.aim += aim

    def update_aim_up(self, aim):
        self.aim -= aim

    def update_horizontal_position(self, horizontal_position):
        self.horizontal_position += horizontal_position

    def update_depth(self, horizontal_position):
        self.depth += self.aim * horizontal_position

    def update_horizontal_position_and_depth(self, horizontal_position):
        self.update_horizontal_position(horizontal_position)
        self.update_depth(horizontal_position)

    def move_with(self, submarine_movements_array):
        for movement in submarine_movements_array:
            direction, value = movement.split()

            {
                FORWARD: self.update_horizontal_position_and_depth,
                DOWN: self.update_aim_down,
                UP: self.update_aim_up
            } [direction](int(value))


def get_submarine_movements_array_from(file):
    submarine_movements_array = []

    with open(file) as my_file:
        submarine_movements_array = my_file.read().split("\n")

    return submarine_movements_array


if "__main__":
    submarine = Submarine()
    submarine_movements_array = get_submarine_movements_array_from(FILE)
    submarine.move_with(submarine_movements_array)
    print(submarine.depth * submarine.horizontal_position)
