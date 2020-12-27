import math
import copy

board = {1:'x', 2:'o', 3:'x',
         4:'o', 5:' ', 6:'o',
         7:' ', 8:'x', 9:'x'}

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n\n\n')


# board = {1:'x', 2:'o', 3:'x',
#          4:'o', 5:' ', 6:'o',
#          7:' ', 8:'x', 9:'x'}

def is_winner(board):
    for i in range(3):
        if board[1 + (i*3)] == board[2 + (i*3)] == board[3 + (i*3)] != ' ':  # horizontal
            return True
        elif board[1 + i] == board[4 + i] == board[7 + i] != ' ':  # vertical
            return True
        elif board[7] == board[5] == board[3] != ' ':  # diagonal
            return True
        elif board[1] == board[5] == board[9] != ' ':  # diagonal
            return True

    return False

def is_tie(board):
    tied = True
    for i in range(9):
        if board[i + 1] == ' ':
            tied = False
    if tied:
        return True
    else:
        return False




def board_eval(board):
    for i in range(3):
        if board[1 + (i*3)] == board[2 + (i*3)] == board[3 + (i*3)] == 'x':  # horizontal
            return 'x'
        elif board[1 + i] == board[4 + i] == board[7 + i] == 'x':  # vertical
            return 'x'
        elif board[7] == board[5] == board[3] == 'x':  # diagonal
            return 'x'
        elif board[1] == board[5] == board[9] == 'x':  # diagonal
            return 'x'

    for i in range(3):
        if board[1 + (i*3)] == board[2 + (i*3)] == board[3 + (i*3)] == 'o':  # horizontal
            return 'o'
        elif board[1 + i] == board[4 + i] == board[7 + i] == 'o':  # vertical
            return 'o'
        elif board[7] == board[5] == board[3] == 'o':  # diagonal
            return 'o'
        elif board[1] == board[5] == board[9] == 'o':  # diagonal
            return 'o'

    else:
        return 'tie'

scores = {'tie':0, 'o':10, 'x':-10}

def minimax(board, depth, is_max, is_first):
    if is_winner(board) or is_tie(board):
        return scores[board_eval(board)] - depth, None

    if is_max:
        max_pos = None
        max_eval = -math.inf
        for pos in range(1, 10):
            if board[pos] == ' ':
                board[pos] = 'o'
                eval, _ = minimax(board, depth+1, False, False)
                if is_first:
                    if eval > max_eval:
                        max_eval = eval
                        max_pos = pos
                else:
                    max_eval = max(max_eval, eval)
                board[pos] = ' '
        return max_eval, max_pos

    else:
        min_eval = math.inf
        for pos in range(1, 10):
            if board[pos] == ' ':
                board[pos] = 'x'
                eval, _ = minimax(board, depth+1, True, False)
                min_eval = min(min_eval, eval)
                board[pos] = ' '
        return min_eval, None

print(minimax(copy.deepcopy(board), 0, True, True))
