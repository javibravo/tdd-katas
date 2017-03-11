class Cell:

    ALIVE = 1
    DEAD = 0

    def __init__(self, status=ALIVE):
        self.status = status

    def evolve(self, live_neighbours):
        if self.status == Cell.ALIVE and (live_neighbours == 2 or live_neighbours == 3):
            self.status = Cell.ALIVE
        elif self.status == Cell.DEAD and live_neighbours == 3:
            self.status = Cell.ALIVE
        else:
            self.status = Cell.DEAD

    def __eq__(self, other):
        return self.status == other.status

    def __ne__(self, other):
        return self.status != other.status

    def __str__(self):
        return str(self.status)