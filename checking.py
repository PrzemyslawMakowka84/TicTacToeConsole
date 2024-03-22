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
        if board_game[i][i] == 'X' or board_game[i][i] == 'O':
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
            x, y = input(
                f'Please enter coordinates(separated by space) for symbol {symbol}(range <1, {board_len}>): ').split(
                ' ')
            x = int(x)
            y = int(y)
            if 0 < x <= board_len and 0 < y <= board_len:
                valid_input = True
            else:
                print(f'Coordinate x or y are out of range! Try again!')
        except ValueError:
            print('You are trying input impermissible character(s)! Try again!')
    return x, y