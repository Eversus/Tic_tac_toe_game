# Условия победы:
def check_winner(board):
    # Проверка по горизонтали
    if board['00'] == board['01'] == board['02'] != ' ':
        return True
    elif board['10'] == board['11'] == board['12'] != ' ':
        return True
    elif board['20'] == board['21'] == board['22'] != ' ':
        return True
    # Проверка по вертикали
    elif board['00'] == board['10'] == board['20'] != ' ':
        return True
    elif board['01'] == board['11'] == board['21'] != ' ':
        return True
    elif board['02'] == board['12'] == board['22'] != ' ':
        return True
    # Проверка по диагонали
    elif board['00'] == board['11'] == board['22'] != ' ':
        return True
    elif board['02'] == board['11'] == board['20'] != ' ':
        return True
    else:
        return False


# Проверяем есть ли свободные поля, если все поля запонены, обьявляем ничью
def check_draw(board):
    for key in board:
        if board[key] == ' ':
            return False
    return True

# Задаём координаты для дальнейшей игры
the_board = {'00': ' ', '01': ' ', '02': ' ',
             '10': ' ', '11': ' ', '12': ' ',
             '20': ' ', '21': ' ', '22': ' '}


# Рисуем доску
def print_board(board):
    print('  0 ' + '1 ' + '2')
    print('0 ' + board['00'] + '|' + board['01'] + '|' + board['02'])
    print('  -+-+-')
    print('1 ' + board['10'] + '|' + board['11'] + '|' + board['12'])
    print('  -+-+-')
    print('2 ' + board['20'] + '|' + board['21'] + '|' + board['22'])


# Начинаем игру
turn = 'X'
for i in range(9):
    print_board(the_board)
    print('Ходят ' + turn + '. Куда ходите?')
    move = input()

    # Проверка на корректность ввода координат и наличие свободной клетки
    while move not in the_board or the_board[move] != ' ':
        print('Некорректный ход. Попробуйте снова.')
        move = input()

    the_board[move] = turn

    # Проверяем есть ли победитель
    if check_winner(the_board):
        print('Поздравляем! Игрок', turn, 'победил!')
        break
    # Если к концу игры все поля заполнены, обьявляем ничью :)
    if check_draw(the_board):
        print('Ничья!')
        break

    # Передаём ход
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
