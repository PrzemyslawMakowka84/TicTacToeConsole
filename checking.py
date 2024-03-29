from colorama import Fore, Style


def check_if_win(board_game: list):
    board_len = len(board_game)
    for i in range(0, board_len):
        if all(cell == 'X' for cell in [board_game[i][cell] for cell in range(board_len)]):
            coloring_winning_symbols(board_game, i, None, 'X')
            return True
        elif all(cell == 'O' for cell in [board_game[i][cell] for cell in range(board_len)]):
            coloring_winning_symbols(board_game, i, None, 'O')
            return True
        if all(cell == 'X' for cell in [board_game[cell][i] for cell in range(board_len)]):
            coloring_winning_symbols(board_game, None, i, 'X')
            return True
        elif all(cell == 'O' for cell in [board_game[cell][i] for cell in range(board_len)]):
            coloring_winning_symbols(board_game, None, i, 'O')
            return True
    temp_list = []
    n = 0
    for i in range(board_len):
        if board_game[i][i] == 'X' or board_game[i][i] == 'O':
            temp_list.append(board_game[i][i])
            n += 1

    if all(cell == 'X' for cell in temp_list) and n == board_len:
        coloring_winning_symbols(board_game, None, None, 'X', True)
        return True
    elif all(cell == 'O' for cell in temp_list) and n == board_len:
        coloring_winning_symbols(board_game, None, None, 'O', True)
        return True

    n = 0
    temp_list = []
    for i in range(board_len):
        if board_game[i][(board_len - 1) - i] == 'X' or board_game[i][(board_len - 1) - i] == 'O':
            temp_list.append(board_game[i][(board_len - 1) - i])
            n += 1

    if all(cell == 'X' for cell in temp_list) and n == board_len:
        coloring_winning_symbols(board_game, None, None, 'X', False)
        return True
    elif all(cell == 'O' for cell in temp_list) and n == board_len:
        coloring_winning_symbols(board_game, None, None, 'O', False)
        return True
    return False


def check_if_draw(board_game: list):
    n = 0
    board_len = len(board_game)
    for i in board_game:
        if_win = check_if_win(board_game)
        if all(cell == 'X' or cell == 'O' for cell in i) and not if_win:
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


def coloring_winning_symbols(board_game, row, col, symbol, is_main_diagonal=True):
    winning_symbol = f'{Fore.LIGHTRED_EX}{symbol}{Style.RESET_ALL}'
    board_len = len(board_game)
    if row is not None:
        for cell in range(board_len):
            board_game[row][cell] = winning_symbol
    elif col is not None:
        for cell in range(board_len):
            board_game[cell][col] = winning_symbol
    elif row is None and col is None and is_main_diagonal:
        for i in range(board_len):
            board_game[i][i] = winning_symbol
    elif row is None and col is None and not is_main_diagonal:
        for i in range(board_len):
            board_game[i][len(board_game) - 1 - i] = winning_symbol


def search_acceptable_fields(playing_board: list):
    coordinates_list = []
    board_len = len(playing_board)
    for i in range(board_len):
        for j in range(board_len):
            if playing_board[i][j] == '*':
                coordinates_list.append([i, j])
    return coordinates_list
