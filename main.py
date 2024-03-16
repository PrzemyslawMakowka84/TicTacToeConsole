def print_board(board_game: list):
    row = 1
    print('  1 2 3')
    for i in board_game:
        print(row, end=' ')
        for j in i:
            print(j, end=' ')
        print()
        row += 1


def check_if_win(board_game: list):
    board_len = len(board_game)
    for i in range(0, board_len):
        if all(cell == 'X' for cell in [board_game[i][cell] for cell in range(board_len)]):
            return True
        elif all(cell == 'O' for cell in [board_game[i][cell] for cell in range(board_len)]):
            return True
        if all(cell == 'X'
 for cell in [board_game[cell][i] for cell in range(board_len)]):
            return True
        elif all(cell == 'O'
 for cell in [board_game[cell][i] for cell in range(board_len)]):
            return True
    temp_list = []
    n = 0
    for i in range(board_len):
        if board_game[i][i] == 'X'or board_game[i][i] == 'O':
            temp_list.append(board_game[i][i])
            n += 1

    if all(cell == 'X' for cell in temp_list) and n == board_len:
        return True
    elif all(cell == 'O' for cell in temp_list) and n == board_len:
        return True

    n = 0
    temp_list = []
    for i in range(board_len):
        if board_game[i][(board_len - 1) - i] == 'X' or board_game[i][(board_len - 1) - i] == 'O':
            temp_list.append(board_game[i][(board_len - 1) - i])
            n += 1

    if all(cell == 'X'
 for cell in temp_list) and n == board_len:
        return True
    elif all(cell == 'O'
 for cell in temp_list) and n == board_len:
        return True
    return False


def check_if_draw(board_game: list):
    n = 0
    board_len = len(board_game)
    for i in board_game:
        if_win = check_if_win(board_game)
        if all(cell == 'X'
 or cell == 'O'
 for cell in i) and not if_win:
            n += 1
    if n == board_len:
        return True
    return False


def check_variables_input(symbol: str, board_len: int):
    x = 0
    y = 0
    valid_input = False
    while not valid_input:
        try:
            x, y = input(f'Please enter coordinates(separated by space) for symbol {symbol}(range <1, {board_len}>): ').split(' ')
            x = int(x)
            y = int(y)
            if 0 < x <= board_len and 0 < y <= board_len:
                valid_input = True
            else:
                print(f'Coordinate x or y are out of range! Try again!')
        except ValueError:
            print('You are trying input impermissible character(s)! Try again!')
    return x, y


def play(board_game: list):
    board_len = len(board_game)
    turn_x = True
    symbol = 'X'

    if_win = check_if_win(board_game)
    if_draw = check_if_draw(board_game)
    while not if_draw and not if_win:
        if turn_x:
            x, y = check_variables_input(symbol, board_len)
            if board_game[x-1][y-1] == 'X' or board_game[x-1][y-1] == 'O':
                print(f"You are trying input symbol {symbol} in the place where is putted 'X' or 'Y'! Try again!")
                print_board(board_game)
                continue
            board_game[x-1][y-1] = 'X'
            symbol = 'O'
            turn_x = False
        else:
            x, y = check_variables_input(symbol, board_len)
            if board_game[x-1][y-1] == 'X' or board_game[x-1][y-1] == 'O':
                print(f"You are trying input symbol {symbol} in the place where is putted 'X' or 'Y'! Try again!")
                print_board(board_game)
                continue
            board_game[x - 1][y - 1] = 'O'
            turn_x = True
            symbol = 'X'

        print_board(board_game)
        if_win = check_if_win(board_game)
        if_draw = check_if_draw(board_game)

    if turn_x:
        symbol = 'O'

    else:
        symbol = 'X'

    print(f'Player who played symbol {symbol} is winner! Congratulations!')


board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print_board(board)
play(board)