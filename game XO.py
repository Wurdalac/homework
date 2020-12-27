board = """
1 | 2 | 3 
----------
4 | 5 | 6
----------
7 | 8 | 9
"""
print(board)
board = list(range (1,10))

def take_input(player):
    while True:
        hod = input('Куда поставить '+ player + '? ')
        if not (hod in '123456789'):
            print('За пределами поля. Повторите ввод')
            continue
        hod = int(hod)
        if str(board[hod - 1]) in 'XO':
            print('Клетка занята другим игроком')
            continue
        board[hod - 1] = player
        break

wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
def win(board):
    for game in wins:
        if (board[game[0] - 1] == board[game[1] - 1] == board[game[2] - 1]):
            return board(game[1] - 1)
    else:
        return False

def main(board):
    counter = 0
    while True:
        board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = win()
            if winner:
                board()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            print('board')
            print('Ничья!')
            break


main(board)
