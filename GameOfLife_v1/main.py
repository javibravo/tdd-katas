from src.grid import Grid
import time

if __name__ == '__main__':
    grid = Grid(10, 10)

    grid.alive(4, 3)
    grid.alive(4, 4)
    grid.alive(4, 5)
    grid.alive(4, 6)
    grid.alive(5, 5)
    grid.alive(4, 5)
    grid.alive(3, 5)
    grid.alive(6, 5)
    grid.alive(5, 3)

    grid.alive(8, 8)
    grid.alive(8, 9)
    grid.alive(8, 7)
    grid.alive(7, 7)
    grid.alive(6, 6)
    grid.alive(7, 8)

    while True:
        print grid
        grid = grid.evolve()
        time.sleep(1)
