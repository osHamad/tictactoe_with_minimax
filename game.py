import copy
import minimax

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n\n\n')


def is_winner(board, turn):
    for i in range(3):
        if board[1 + (i*3)] == board[2 + (i*3)] == board[3 + (i*3)] != ' ':  # horizontal
            print(f'{turn} won')
            return True

        elif board[1 + i] == board[4 + i] == board[7 + i] != ' ':  # vertical
            print(f'{turn} won')
            return True

        elif board[7] == board[5] == board[3] != ' ':  # diagonal
            print(f'{turn} won')
            return True

        elif board[1] == board[5] == board[9] != ' ':  # diagonal
            print(f'{turn} won')
            return True

    else:
        return False


def is_tie(board):
    tied = True
    for i in range(1, 10):
        if board[i] == ' ':
            tied = False
    if tied:
        print('it\'s a tie.')
        return True

    else:
        return False


def player_play(board):
    while True:
        play = int(input('your turn: '))
        if 0 < play <= 9:
            if board[play] == ' ':
                return play
            else:
                print('spot is taken')
        else:
            print('out of range')

def cpu_play(board):
    for i in range(1,10):
        if board[i] == ' ':
            return i


def main():
    player = 'x'
    cpu = 'o'

    tie = False
    won = False

    board = {
        1:' ', 2:' ', 3:' ',
        4:' ', 5:' ', 6:' ',
        7:' ', 8:' ', 9:' '
    }

    current_player = player
    while not won and not tie:
        try:
            print_board(board)
            if current_player == player:
                board[player_play(board)] = current_player
            else:
                board[minimax.minimax(copy.deepcopy(board), 0, True, True)[1]] = current_player

            tie = is_tie(board)
            won = is_winner(board, current_player)

            if current_player == player:
                current_player = cpu
            else:
                current_player = player

        except ValueError:
            print('input a valid move')

    print_board(board)


if __name__ == '__main__':
    main()
