class Cell:

    ALIVE = 1
    DEAD = 0

    def __init__(self, status=ALIVE):
        self.status = status

    def next_stage(self, live_neighbours):
        if self.status == Cell.ALIVE and (live_neighbours == 2 or live_neighbours == 3):
            self.status = Cell.ALIVE
        elif self.status == Cell.DEAD and live_neighbours == 3:
            self.status = Cell.ALIVE
        else:
            self.status = Cell.DEAD
