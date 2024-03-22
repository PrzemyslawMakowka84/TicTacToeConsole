def print_board(board_game: list):
    row = 1
    bord_len = len(board_game)
    print(' ', end='')
    for i in range(bord_len):
        print(f' {i + 1}', end='')
    print()
    for i in board_game:
        print(row, end=' ')
        for j in i:
            print(j, end=' ')
        print()
        row += 1