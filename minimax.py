import math
import conditions

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


def minimax(board, depth, is_max, is_first):
    scores = {'tie':0, 'o':10, 'x':-10}

    if conditions.is_winner(board, None, False) or conditions.is_tie(board, False):
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
