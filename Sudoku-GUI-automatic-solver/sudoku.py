import pygame
from random import randrange

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

WIDTH = 1200
HEIGHT = 800
rec_size = 75
border = 50

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku solver')
clock = pygame.time.Clock()


def draw_board():
    '''drawing board on screen '''
    for i in range(0, 9):
        for j in range(0, 9):
            pygame.draw.rect(gameDisplay, white, pygame.Rect(
                    border+(i*rec_size), border+(j*rec_size),
                    rec_size, rec_size), 2)
            pygame.display.flip()


def draw_number(board: list, user_number: int, rows: int, columns: int):
    '''draws number in right rectangle'''
    textsurface = myfont.render(str(user_number), False, white)
    board[rows][columns] = int(user_number)
    x = border + (rows*rec_size) + (rec_size / 3)
    y = border + (columns*rec_size) + (rec_size / 4)
    gameDisplay.blit(textsurface, (x, y))
    pygame.display.update()
    return board


def fill_board(board: list):
    '''fills first numbers to board'''
    not_deletable = []
    for i in range(0, 3):
        for j in range(0, 3):
            is_valid = False
            while is_valid is False:
                user_number = randrange(1, 10)
                a = (i*3)+randrange(0, 3)
                b = (j*3)+randrange(0, 3)
                not_deletable.append((a, b))
                is_valid = check_number(board, user_number, a, b)
            board = draw_number(board, user_number, a, b)

    return board, not_deletable


def check_number(board: list, user_in: int, a: int, b: int):
    '''checks if number compatible with sudoku rules
    and returns bool of result; takes board which is [9x9] list'''

    if board[a][b] != 0:
        return False

# checks rows and columns of board
    if user_in in board[a]:
        return False

    temp_set = set()
    for i in board:
        temp_set.add(i[b])
        if user_in in temp_set:
            return False

    a = a//3
    b = b//3
# checks [3x3] matrixes of board
    for i in range(a * 3, a * 3 + 3):
        for j in range(b * 3, b * 3 + 3):
            # checking if number is present in 3x3 rectangles
            if board[i][j] == int(user_in):
                return False

    return True


def to_columns(x: int, y: int):
    '''Calculate from position to rectangles'''
    row = (x-(x % rec_size)) / rec_size
    column = (y-(y % rec_size)) / rec_size
    row = max(0, min(row, 8))
    column = max(0, min(column, 8))

    return (int(row), int(column))


def clear_rec_by_cols(board: list, a: int, b: int) -> None:
    '''clears rectangle based on columns on screen'''

    myRec = pygame.Rect(
        border+(a*rec_size), border+(b*rec_size), rec_size, rec_size)

    pygame.draw.rect(gameDisplay, black, myRec)
    pygame.draw.rect(gameDisplay, white, myRec, 2)
    board[a][b] = 0


def clear_rec(board: list, x: int, y: int, not_delete: list) -> list:
    '''clears rectangle based on position on screen'''
    (a, b) = to_columns(x, y)
    if (a, b) in not_delete:
        return board

    myRec = pygame.Rect(
        x, y, rec_size, rec_size)

    pygame.draw.rect(gameDisplay, black, myRec)
    board[a][b] = 0
    select_rectangle(x, y, 'W', (x, y))
    return board


def check_limit(x, y):
    ''' Checks limit of posible rectangle highliting'''
    if x < 50 or x > (rec_size*8)+border:
        return False
    elif y < 50 or y > (rec_size*8)+border:
        return False
    return True


def select_rectangle(x: int, y: int, prev_color: str, prev_position):
    '''selects rectangle with red colorand returns coulor and position
     of now selected rectangle'''

# calculates position to draw rectangle
    (x, y) = (x-((x-border) % rec_size), y-((y-border) % rec_size))

# short names for rectangles to draw
    prevRec = pygame.Rect(
        prev_position[0], prev_position[1], rec_size, rec_size)
    myRec = pygame.Rect(
        x-((x-border) % rec_size),
        y-((y-border) % rec_size), rec_size, rec_size)

# checks if position is on board
    if check_limit(x, y) is False:
        return prev_color, prev_position

# checks if position matches with previous position to change colours
# or in last elif changes coulor if other rect is clicked
    if prev_color == 'W':
        pygame.draw.rect(gameDisplay, red, myRec, 2)
        prev_color = 'R'
    elif prev_color == 'R' and (x, y) == prev_position:
        pygame.draw.rect(gameDisplay, white, myRec, 2)
        prev_color = 'W'
    elif prev_color == 'R' and (x, y) != prev_position:
        pygame.draw.rect(gameDisplay, white, prevRec, 2)
        pygame.draw.rect(gameDisplay, red, myRec, 2)
        prev_color = 'R'

    return prev_color, (x, y)


def main():
    crashed = False

    draw_board()
    board = []
    [board.append([0, 0, 0, 0, 0, 0, 0, 0, 0]) for i in range(0, 9)]
    board, not_delete = fill_board(board)

    prev_color = 'W'
    prev_position = (border, border)

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                (mouse_wid, mouse_hei) = pygame.mouse.get_pos()
                prev_color, prev_position = select_rectangle(
                    mouse_wid, mouse_hei, prev_color, prev_position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and prev_color == 'R':
                    board = clear_rec(
                        board, prev_position[0], prev_position[1], not_delete)
                if event.unicode.isnumeric() is True and prev_color == 'R':
                    if check_limit(prev_position[0], prev_position[1]) is True:
                        (a, b) = to_columns(prev_position[0], prev_position[1])
                        user_num = int(event.unicode)
                        if check_number(board, user_num, a, b) is True:
                            board = draw_number(board, event.unicode, a, b)
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
