from cell import Cell


class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[Cell(Cell.DEAD) for j in range(y)] for i in range(x)]

    def evolve(self):
        evolved_grid = Grid(self.x, self.y)
        evolved_grid.grid = [[self.grid[i][j] for j in range(self.y)] for i in range(self.x)]
        evolved_grid.alive(1, 1)
        return evolved_grid


    def alive(self, x, y):
        self.grid[x][y] = Cell.ALIVE