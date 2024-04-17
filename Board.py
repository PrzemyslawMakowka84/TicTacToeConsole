from colorama import Fore, Style
from random import randint


class Board:
    def __init__(self, size: int):
        self.__playing_with_computer = Board.__choosing_play_with_computer()
        if self.__playing_with_computer:
            self.__symbol_play_human = Board.__choosing_play_symbol()
        match size:
            case 3:
                self.__len_of_board = 3
                self.__board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
            case 4:
                self.__len_of_board = 4
                self.__board = [
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*']
                ]
            case 5:
                self.__len_of_board = 5
                self.__board = [
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*']
                ]

    def __print_board(self):
        row = 1
        print(' ', end='')
        for i in range(self.__len_of_board):
            print(f' {i + 1}', end='')
        print()
        for row_board in self.__board:
            print(row, ' '.join(row_board))
            row += 1

    def play(self):
        turn_x = True
        turn_o = False
        symbol = 'X'
        if_win = False
        if_draw = False
        self.__print_board()
        play_longer = True
        while play_longer and not (if_draw and not if_win):
            if turn_x and self.__symbol_play_human == 'X':
                x, y = self.__check_variables_input(symbol)
                if self.__board[x - 1][y - 1] == 'X' or self.__board[x - 1][y - 1] == 'O':
                    putted_symbol = self.__board[x - 1][y - 1]
                    print(
                        f"You are trying input symbol {symbol} in the place where is putted '{putted_symbol}'! "
                        f"Try again!")
                    self.__print_board()
                    continue
                self.__board[x - 1][y - 1] = symbol
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                if turn_x:
                    turn_x = False
                    turn_o = True
                    symbol = 'O'
                elif turn_o:
                    turn_x = True
                    turn_o = False
                    symbol = 'X'
            elif turn_o and self.__symbol_play_human == 'O':
                x, y = self.__check_variables_input(symbol)
                if self.__board[x - 1][y - 1] == 'X' or self.__board[x - 1][y - 1] == 'O':
                    putted_symbol = self.__board[x - 1][y - 1]
                    print(
                        f"You are trying input symbol {symbol} in the place where is putted '{putted_symbol}'! "
                        f"Try again!")
                    self.__print_board()
                    continue
                self.__board[x - 1][y - 1] = symbol
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                if turn_x:
                    turn_x = False
                    turn_o = True
                    symbol = 'O'
                elif turn_o:
                    turn_x = True
                    turn_o = False
                    symbol = 'X'
            elif turn_o and (self.__playing_with_computer and self.__symbol_play_human != 'X'):
                coordinate_fields = self.__search_acceptable_fields()
                rand = randint(0, len(coordinate_fields) - 1)
                self.__board[coordinate_fields[rand][0]][coordinate_fields[rand][1]] = 'O'
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                turn_x = True
                turn_o = False
                symbol = 'X'
            elif turn_o and (self.__playing_with_computer and self.__symbol_play_human != 'O'):
                coordinate_fields = self.__search_acceptable_fields()
                rand = randint(0, len(coordinate_fields) - 1)
                self.__board[coordinate_fields[rand][0]][coordinate_fields[rand][1]] = 'O'
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                turn_x = True
                turn_o = False
                symbol = 'X'
            elif turn_x and (self.__playing_with_computer and self.__symbol_play_human != 'O'):
                coordinate_fields = self.__search_acceptable_fields()
                rand = randint(0, len(coordinate_fields) - 1)
                self.__board[coordinate_fields[rand][0]][coordinate_fields[rand][1]] = 'X'
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                turn_x = False
                turn_o = True
                symbol = 'O'
            elif turn_x and (self.__playing_with_computer and self.__symbol_play_human != 'X'):
                coordinate_fields = self.__search_acceptable_fields()
                rand = randint(0, len(coordinate_fields) - 1)
                self.__board[coordinate_fields[rand][0]][coordinate_fields[rand][1]] = 'X'
                if_win = self.__check_if_win(symbol)
                if if_win:
                    self.__print_board()
                    print(f'Player who played symbol {symbol} is winner! Congratulations!')
                    play_longer = False
                    continue
                turn_x = False
                turn_o = True
                symbol = 'O'
            if_draw = self.__check_if_draw(symbol)
            self.__print_board()
        if if_draw:
            print(f'This time we have a draw! Thanks you for enjoying!')

    def __coloring_winning_symbols(self, row, col, symbol, is_main_diagonal=True):
        winning_symbol = f'{Fore.LIGHTRED_EX}{symbol}{Style.RESET_ALL}'
        board_len = len(self.__board)
        if row is not None:
            for cell in range(board_len):
                self.__board[row][cell] = winning_symbol
        elif col is not None:
            for cell in range(board_len):
                self.__board[cell][col] = winning_symbol
        elif row is None and col is None and is_main_diagonal:
            for i in range(board_len):
                self.__board[i][i] = winning_symbol
        elif row is None and col is None and not is_main_diagonal:
            for i in range(board_len):
                self.__board[i][len(self.__board) - 1 - i] = winning_symbol

    def __check_if_draw(self, symbol: str):
        n = 0
        board_len = len(self.__board)
        for i in self.__board:
            if_win = self.__check_if_win(symbol)
            if all(cell == 'X' or cell == 'O' for cell in i) and not if_win:
                n += 1
        if n == board_len:
            return True
        return False

    def __check_if_win(self, symbol: str):
        board_len = len(self.__board)
        for i in range(0, board_len):
            if all(cell == symbol for cell in [self.__board[i][cell] for cell in range(board_len)]):
                self.__coloring_winning_symbols(i, None, symbol)
                return True
            elif all(cell == symbol for cell in [self.__board[cell][i] for cell in range(board_len)]):
                self.__coloring_winning_symbols(None, i, symbol)
                return True
            elif all(cell == symbol for cell in [self.__board[cell][cell] for cell in range(board_len)]):
                self.__coloring_winning_symbols(None, None, symbol, True)
                return True
            elif all(cell == symbol for cell in [self.__board[i][(board_len - 1) - i] for i in range(board_len)]):
                self.__coloring_winning_symbols(None, None, symbol, False)
                return True
        return False

    def __check_variables_input(self, symbol: str):
        x = 0
        y = 0
        valid_input_not_clear = True
        while valid_input_not_clear:
            try:
                x, y = input(f'Please enter coordinates(separated by space) '
                             f'for symbol {symbol}(range <1, {self.__len_of_board}>): ').split(" ")
                if str.isdigit(x) and str.isdigit(y):
                    x = int(x)
                    y = int(y)
                    if (0 < x <= self.__len_of_board) and (0 < y <= self.__len_of_board):
                        valid_input_not_clear = False
                    else:
                        print(f'Coordinate x or y are out of range! Try again!')
                else:
                    print(f'You are inputted characters instead of numbers! Try again!')
            except ValueError:
                print('You are trying input impermissible character(s)! Try again!')
            if valid_input_not_clear:
                self.__print_board()
        return x, y

    def __search_acceptable_fields(self):
        coordinates_list = []
        for i in range(self.__len_of_board):
            for j in range(self.__len_of_board):
                if self.__board[i][j] == '*':
                    coordinates_list.append([i, j])
        return coordinates_list

    @staticmethod
    def __choosing_play_with_computer():
        return Board.__helper_chose(
            "Do you want play with computer?(y/n): ",
            "Please type 'y' or 'n': ",
            "y",
            "n"
        )

    @staticmethod
    def __choosing_play_symbol():
        return Board.__helper_chose(
            "With symbol do you want to play('X' or 'O'): ",
            "Please type 'X', or 'O': ",
            "X",
            "O"
        )

    @staticmethod
    def __helper_chose(message1: str, message2: str, symbol1: str, symbol2: str):
        answer = input(message1)
        while not (answer in [f'{symbol1}', f'{symbol2}']) and (len(answer) >= 1):
            answer = input(message2)
        if symbol1 in ('X', 'Y'):
            return answer
        else:
            return True if answer == 'y' else False

    @staticmethod
    def choose_size_board():
        size = 0
        lower_size = 2
        upper_size = 5
        while lower_size >= size or size > upper_size:
            try:
                size = int(input('Enter a board size from range<3, 5>: '))
                if lower_size >= size or size > upper_size:
                    print('You are trying to enter size from no acceptable range! Try again!')
            except ValueError:
                print('You entered not acceptable characters! Try again!')
        return size
