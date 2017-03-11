from src.board import Board


def test_dead_cell_come_alive():
    board = Board(3, 3)
    board.alive(0, 0)
    board.alive(0, 1)
    board.alive(1, 0)

    evolved_board = board.evolve()

    expected_evolved_board = Board(3, 3)
    expected_evolved_board.alive(0, 0)
    expected_evolved_board.alive(0, 1)
    expected_evolved_board.alive(1, 0)
    expected_evolved_board.alive(1, 1)

    assert evolved_board == expected_evolved_board


def test_alive_cell_come_dead():
    board = Board(3, 3)
    board.alive(0, 0)
    board.alive(0, 1)

    evolved_board = board.evolve()

    expected_evolved_board = Board(3, 3)

    assert evolved_board == expected_evolved_board
