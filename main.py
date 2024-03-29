import random
import printing
import checking
import choosing


def play(board_game: list, playing_with_computer=False):
    board_len = len(board_game)
    turn_x = True
    turn_o = False
    symbol = 'X'
    if_win = False
    if_draw = False
    while not if_draw and not if_win:
        if turn_x or (turn_o != playing_with_computer):
            x, y = checking.check_variables_input(symbol, board_len)
            if board_game[x - 1][y - 1] == 'X' or board_game[x - 1][y - 1] == 'O':
                putted_symbol = board_game[x - 1][y - 1]
                print(f"You are trying input symbol {symbol} in the place where is putted '{putted_symbol}'! Try again!")
                printing.print_board(board_game)
                continue
            board_game[x - 1][y - 1] = symbol
            if_win = checking.check_if_win(board_game, symbol)
            if if_win:
                printing.print_board(board_game)
                print(f'Player who played symbol {symbol} is winner! Congratulations!')
                break
            if turn_x:
                turn_x = False
                turn_o = True
                symbol = 'O'
            elif turn_o:
                turn_x = True
                turn_o = False
                symbol = 'X'
        elif playing_with_computer and turn_o:
            coordinate_fields = checking.search_acceptable_fields(board_game)
            rand = random.randint(0, len(coordinate_fields) - 1)
            board_game[coordinate_fields[rand][0]][coordinate_fields[rand][1]] = 'O'
            if_win = checking.check_if_win(board_game, symbol)
            if if_win:
                printing.print_board(board_game)
                print(f'Player who played symbol {symbol} is winner! Congratulations!')
                break
            turn_x = True
            turn_o = False
            symbol = 'X'
        if_draw = checking.check_if_draw(board_game, symbol)
        printing.print_board(board_game)
    if if_draw:
        print(f'This time we have a draw! Thanks you for enjoying!')


playing_with_computer = choosing.choosing_player()
board = choosing.choose_size_board()
printing.print_board(board)
play(board, playing_with_computer)
