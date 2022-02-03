from sudokusolver import sudoku


def test_sudoku():

    assert sudoku.to_columns(sudoku.rec_size+1, sudoku.rec_size+1) == (1, 1)