from src.cell import Cell


def test_alive_cell_with_fewer_fewer_2_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 1

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DIED


def test_alive_cell_with_more_than_3_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    live_neighbours = 4

    cell.next_stage(live_neighbours)

    assert cell.status == Cell.DIED


