''' pytesting '''
import pytest
import test_values
from sudokusolver import sudoku


def test_sudoku():
    ''' testing sudoku gui'''
    assert sudoku.to_columns(sudoku.rec_size+1, sudoku.rec_size+1) == (1, 1)


@pytest.mark.skip(reason="This can be seen during testing app")
def test_draw_board():
    ''' test draw function'''
    assert sudoku.draw_board() is None


def test_fill_board():
    ''' test filling numbers function'''
    temp_board, not_del = sudoku.fill_board(test_values.empty_board)

    numbers_count = 0
    zeros = 0
    for i in temp_board:
        zeros += i.count(0)
        assert len(i) == 9
        for j in i:
            if j != 0:
                numbers_count += 1

    assert numbers_count == 9
    assert zeros == 72
    assert len(not_del) == 9
    assert len(temp_board) == 9


@pytest.mark.parametrize("board, user_in, row, col, expected",[
(test_values.board, 1, 0, 0, False),
(test_values.board, 1, 0, 6, False),
(test_values.board, 1, 6, 0, False),
(test_values.board, 1, 1, 2, False),
(test_values.board, 1, 3, 1, True),
(test_values.board, 1, 6, 1, True),
(test_values.board, 1, 1, 6, True)
])

def test_checking_number(board, user_in, row, col, expected):
    ''' test checking numbers function'''
    assert sudoku.check_number(board, user_in, row, col) is expected


@pytest.mark.parametrize("board, user_in, row, col, expected",[
(test_values.board, 1, 0, 1, test_values.added_num_board),
(test_values.board, 4, 8, 0, test_values.added_sec_num_board)
])

def test_inserting_number(board, user_in, row, col, expected):
    ''' test inserting numbers function'''
    assert sudoku.draw_number(board, user_in, row, col) == expected

@pytest.mark.parametrize("x, y, expected",[
(2, 3, (0,0)),
(sudoku.rec_size +1, sudoku.rec_size +1, (1,1)),
(5*sudoku.rec_size +1, 5*sudoku.rec_size +1, (5,5)),
(9*sudoku.rec_size +1, 9*sudoku.rec_size +1, (8,8)),
])
def test_to_colums(x, y, expected):
    ''' testing to columns feature '''
    assert sudoku.to_columns(x, y) == expected


def test_clear_rectangle_by_columns():
    ''' testing clear rectangle by columns function '''

    sudoku.clear_rec_by_cols(test_values.added_num_board, 1, 1)
    assert test_values.added_num_board[1][1] == 0


def test_clear_rectangle_by_position():
    ''' testing clearing rectangle by position function '''
    board = sudoku.clear_rec(test_values.added_num_board, 51, 51, test_values.added_num_not_delete)
    assert board[1][1] == 0

@pytest.mark.parametrize("x, y, expected",[
(0, sudoku.border + 1, False),
(sudoku.border + 1, 0, False),
(sudoku.border + 1, sudoku.border + 1, True),
((sudoku.rec_size * 8) + sudoku.border, (sudoku.rec_size * 8) + sudoku.border + 1, False)
])
def test_check_limit(x, y, expected):
    ''' Test ranges to highlight on screen '''
    assert sudoku.check_limit(x, y) is expected


@pytest.mark.parametrize("x, y, prev_color, prev_position, expected",[
(sudoku.border +1 , sudoku.border + 1, 'W', (0, 0), ('R', (sudoku.border, sudoku.border))),
(sudoku.border +1 , sudoku.border + 1, 'R', (sudoku.border, sudoku.border), ('W', (sudoku.border, sudoku.border))),
(sudoku.border +1 , sudoku.border + 1, 'R', (sudoku.border + 300, sudoku.border + 300), ('R', (sudoku.border, sudoku.border)))
])
def test_selecting_rectangle(x, y, prev_color, prev_position, expected):
    ''' test selecting rectangle function '''
    assert sudoku.select_rectangle(x, y, prev_color, prev_position) == expected


@pytest.mark.skip(reason="main function")
def test_main():
    ''' main function test '''
    sudoku.main()
    print("tested")
    