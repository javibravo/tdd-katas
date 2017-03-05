from src.cell import Cell


def test_alive_cell_with_fewer_than_1_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 1

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DIED


def test_alive_cell_with_fewer_than_0_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 0

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DIED

