import math

board = {1:'x', 2:'o', 3:'x', 4:'o', 5:' ', 6:'o', 7:'o', 8:' ', 9:'x'}

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n\n\n')

def is_winner(board):
    for i in range(3):
        if board[1 + i] == board[2 + i] == board[3 + i] != ' ':  # horizontal
            return True
        elif board[1 + i] == board[4 + i] == board[7 + i] != ' ':  # vertical
            return True
        elif board[7] == board[5] == board[3] != ' ':  # diagonal
            return True
        elif board[1] == board[5] == board[9] != ' ':  # diagonal
            return True
    else:
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
        if board[1 + i] == board[2 + i] == board[3 + i] == 'x':  # horizontal
            return 'x'
        elif board[1 + i] == board[4 + i] == board[7 + i] == 'x':  # vertical
            return 'x'
        elif board[7] == board[5] == board[3] == 'x':  # diagonal
            return 'x'
        elif board[1] == board[5] == board[9] == 'x':  # diagonal
            return 'x'

    for i in range(3):
        if board[1 + i] == board[2 + i] == board[3 + i] == 'o':  # horizontal
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

def minimax(board, depth, is_max):
    if is_winner(board) or is_tie(board):
        return scores[board_eval(board)] - depth

    if is_max:
        max_eval = -math.inf
        for pos in range(1, 10):
            if board[pos] == ' ':
                board[pos] = 'o'
                eval = minimax(board, depth+1, False)
                max_eval = max(max_eval, eval)
                board[pos] = ' '
        return max_eval

    else:
        min_eval = math.inf
        for pos in range(1, 10):
            if board[pos] == ' ':
                board[pos] = 'x'
                eval = minimax(board, depth+1, True)
                min_eval = min(min_eval, eval)
                board[pos] = ' '
        return min_eval

print(minimax(board, 0, True))
