def solve(board):
    
    empty_cell = find_empty_cell(board)
    if empty_cell:
        row, col = empty_cell
    else:
        return True

    #Sudoku only allows numbers between 1 and 9
    for i in range(1,10):
        if is_valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def is_valid(board, pos, num):
    """
    Returns true same number isn't found in the same row, volumn or grid
    """

    # Check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check 3x3 grid
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True



def find_empty_cell(board):
    """
    finds the empty cell going left to right, top to bottom on the board
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_board(board):
    for i in board:
        print(" ".join(map(str, i)))

game_board = [
    [0,0,0,8,0,0,5,9,3],
    [5,1,0,0,0,0,0,2,0],
    [0,0,8,9,4,5,7,0,0],
    [7,3,0,0,0,2,0,0,6],
    [0,5,6,0,0,0,1,4,0],
    [2,0,0,6,0,0,0,7,9],
    [0,0,3,4,1,7,2,0,0],
    [0,7,0,0,0,0,0,3,4],
    [8,4,5,0,0,6,0,0,0],
]

solve(game_board)

print_board(game_board)