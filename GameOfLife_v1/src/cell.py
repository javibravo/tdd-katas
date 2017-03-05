class Cell:

    ALIVE = 1
    DIED = 0

    def __init__(self, status=ALIVE):
        self.status = status

    def next_stage(self, neighbours):
        self.status = Cell.DIED
