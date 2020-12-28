def is_winner(board, turn, print_msg):
    for i in range(3):
        if board[1 + (i*3)] == board[2 + (i*3)] == board[3 + (i*3)] != ' ':  # horizontal
            if print_msg:
                print(f'{turn} won')
            return True

        elif board[1 + i] == board[4 + i] == board[7 + i] != ' ':  # vertical
            if print_msg:
                print(f'{turn} won')
            return True

        elif board[7] == board[5] == board[3] != ' ':  # diagonal
            if print_msg:
                print(f'{turn} won')
            return True

        elif board[1] == board[5] == board[9] != ' ':  # diagonal
            if print_msg:
                print(f'{turn} won')
            return True

    return False


def is_tie(board, print_msg):
    tied = True
    for i in range(1, 10):
        if board[i] == ' ':
            tied = False
    if tied:
        if print_msg:
            print('it\'s a tie.')
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
