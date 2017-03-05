from src.cell import Cell


def test_alive_cell_with_fewer_than_2_neighbours_dies():
    cell = Cell(Cell.ALIVE)
    neighbours = 1

    cell.next_stage(neighbours)

    assert cell.status == Cell.DIED
