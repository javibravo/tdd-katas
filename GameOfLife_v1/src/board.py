from cell import Cell


class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[Cell(Cell.DEAD) for j in range(y)] for i in range(x)]

    def evolve(self):
        evolved_board = Board(self.x, self.y)

        for i in range(self.x):
            for j in range(self.y):
                evolved_board.grid[i][j].status = self.grid[i][j].status
                evolved_board.grid[i][j].evolve(self.number_of_live_neighbours(i, j))

        return evolved_board

    def alive(self, x, y):
        self.grid[x][y].status = Cell.ALIVE

    def number_of_live_neighbours(self, i, j):
        i_neighbours_indexes = self.get_valid_indexed(i, self.x)
        j_neighbours_indexes = self.get_valid_indexed(j, self.y)
        live_neighbours = 0
        for k_index in range(len(i_neighbours_indexes)):
            for l_index in range(len(j_neighbours_indexes)):
                k = i_neighbours_indexes[k_index]
                l = j_neighbours_indexes[l_index]
                if k == i and l == j:
                    continue
                if self.grid[k][l].status == Cell.ALIVE:
                    live_neighbours += 1
        return live_neighbours

    def get_valid_indexed(self, i, max):
        valid_indexes = []
        if i - 1 >= 0:
            valid_indexes.append(i - 1)
        valid_indexes.append(i)
        if i + 1 < max:
            valid_indexes.append(i + 1)
        return valid_indexes

    def __eq__(self, other):
        if not (self.x == other.x and self.y == other.y):
            return False

        for i in range(self.x):
            for j in range(self.y):
                if self.grid[i][j] != other.grid[i][j]:
                    return False

        return True

    def __str__(self):
        output = ""
        for i in range(self.x):
            output += "[  "
            for j in range(self.y):
                output += "{}  ".format(self.grid[i][j])
            output += "]\n"
        return output
