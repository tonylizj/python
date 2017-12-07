# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    def eat_sprout(self):
        self.num_sprouts_eaten += 1

    def __str__(self):
        return self.symbol + " at (" + str(self.row) + ", " + str(self.col) + ") ate " + str(self.num_sprouts_eaten) + " sprouts."


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for row in range(len(maze)):
            for col in maze[row]:
                if col == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, col):
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        if row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        elif row == self.rat_2.row and col == self.rat_2.col:
            return self.rat_2.symbol
        elif self.maze[row][col] == HALL:
            return HALL
        else:
            return self.maze[row][col]

    def move(self, rat, v_change, h_change):
        target = self.maze[rat.row+v_change][rat.col+h_change]
        if target == WALL:
            return False
        else:
            if target == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left -= 1
                self.maze[rat.row+v_change][rat.col+h_change] = HALL

            rat.set_location(rat.row+v_change, rat.col+h_change)
            return True

    def __str__(self):
        return str(self.maze) + "\n" + self.rat_1.__str__() + "\n" + self.rat_2.__str__()
