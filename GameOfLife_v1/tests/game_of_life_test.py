from src.cell import Cell


def test_alive_cell_with_fewer_fewer_2_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 1

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DEAD


def test_alive_cell_with_more_than_3_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 4

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DEAD


def test_alive_cell_with_2_neighbours_keep_alive():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 2

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.ALIVE


def test_alive_cell_with_3_neighbours_keep_alive():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 3

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.ALIVE


def test_dead_cell_with_3_neighbours_change_to_live():
    cell = Cell(Cell.DEAD)
    live_neighbours = 3

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.ALIVE


def test_dead_cell_with_2_neighbours_keep_dead():
    cell = Cell(Cell.DEAD)
    live_neighbours = 2

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DEAD


