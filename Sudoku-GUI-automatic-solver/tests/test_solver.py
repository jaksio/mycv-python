''' test sudoku backtracing solver '''
import test_values
import pytest
from sudokusolver import solver
from sudokusolver import sudoku

def test_find_empty():
    ''' test find empty function '''
    assert solver.find_empty(test_values.board) == (0,1)
    assert solver.find_empty(test_values.board_test_find) == (0,4)


@pytest.mark.skip(reason="No need to test main")
def test_main():
    ''' main testing'''
    solver.main()


def solve_quick(board: list[list[int]]) -> bool:
    ''' remade solve from solver without gui interface and sleep() functions inside '''
    find = solver.find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if sudoku.check_number(board, i, row, col):
            board[row][col] = i
            if solve_quick(board):
                return True
            board[row][col] = 0

    return False


def test_solver():
    ''' test main solving function '''
    assert solve_quick(test_values.test_solved_board) is True
    solve_quick(test_values.test_solver_board)
    assert test_values.test_solver_board == test_values.test_solved_board
    assert solve_quick(test_values.test_solver_board) is True
