from src.grid import Grid


def test_dead_cell_come_alive():
    grid = Grid(3, 3)
    grid.alive(0, 0)
    grid.alive(0, 1)
    grid.alive(1, 0)

    evolved_grid = grid.evolve()

    expected_evolved_grid = Grid(3, 3)
    expected_evolved_grid.alive(0, 0)
    expected_evolved_grid.alive(0, 1)
    expected_evolved_grid.alive(1, 0)
    expected_evolved_grid.alive(1, 1)

    assert evolved_grid == expected_evolved_grid


def test_alive_cell_come_dead():
    grid = Grid(3, 3)
    grid.alive(0, 0)
    grid.alive(0, 1)

    evolved_grid = grid.evolve()

    expected_evolved_grid = Grid(3, 3)

    assert evolved_grid == expected_evolved_grid
