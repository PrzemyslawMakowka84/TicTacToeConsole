import print_board
import checking


def play(board_game: list):
    board_len = len(board_game)
    turn_x = True
    symbol = 'X'

    if_win = checking.check_if_win(board_game)
    if_draw = checking.check_if_draw(board_game)
    while not if_draw and not if_win:
        if turn_x:
            x, y = checking.check_variables_input(symbol, board_len)
            if board_game[x - 1][y - 1] == 'X':
                print(f"You are trying input symbol {symbol} in the place where is putted 'X'! Try again!")
                print_board.print_board(board_game)
                continue
            elif board_game[x - 1][y - 1] == 'O':
                print(f"You are trying input symbol {symbol} in the place where is putted 'O'! Try again!")
                print_board.print_board(board_game)
                continue
            board_game[x - 1][y - 1] = 'X'
            symbol = 'O'
            turn_x = False
        else:
            x, y = checking.check_variables_input(symbol, board_len)
            if board_game[x - 1][y - 1] == 'X':
                print(f"You are trying input symbol {symbol} in the place where is putted 'X'! Try again!")
                print_board.print_board(board_game)
                continue
            elif board_game[x - 1][y - 1] == 'O':
                print(f"You are trying input symbol {symbol} in the place where is putted 'O'! Try again!")
                print_board.print_board(board_game)
                continue
            board_game[x - 1][y - 1] = 'O'
            turn_x = True
            symbol = 'X'

        print_board.print_board(board_game)
        if_win = checking.check_if_win(board_game)
        if_draw = checking.check_if_draw(board_game)

    if turn_x and if_win:
        symbol = 'O'
        print(f'Player who played symbol {symbol} is winner! Congratulations!')
    elif not turn_x and if_win:
        symbol = 'X'
        print(f'Player who played symbol {symbol} is winner! Congratulations!')
    if if_draw:
        print(f'This time we have a draw! Thanks you for enjoying!')


board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print_board.print_board(board)
play(board)