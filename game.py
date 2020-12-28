import copy
import minimax
import conditions

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n\n\n')

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

            tie = conditions.is_tie(board, True)
            won = conditions.is_winner(board, current_player, True)

            if current_player == player:
                current_player = cpu
            else:
                current_player = player

        except ValueError:
            print('input a valid move')

    print_board(board)


if __name__ == '__main__':
    main()
