import sudoku
import pygame
from time import sleep
from typing import Union


def find_empty(board: list[list[int]]) -> Union[tuple[int, int], None]:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def solve(board: list[list[int]]) -> bool:
    """Solves given board drawing for user to see"""
    # Finds empty field in 9x9 board
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # number 1 - 9
    for i in range(1, 10):
        # if compatible with sudoku rules
        if sudoku.check_number(board, i, row, col):
            # draw and enter to board
            board = sudoku.draw_number(board, i, row, col)
            sleep(0.5)
            # if not another empty field found end
            # else recursion for another field
            if solve(board):
                return True
            # clear this number because no solve true found
            sudoku.clear_rec_by_cols(board, row, col)
            sleep(0.5)

    return False


def main():
    crashed = False

    sudoku.draw_board()
    board = []
    for i in range(0, 9):
        board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    board, not_delete = sudoku.fill_board(board)

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                solve(board)
                print(board)
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        sudoku.clock.tick(60)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
