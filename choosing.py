def choose_size_board():
    size = 0
    while 2 >= size or size > 5:
        try:
            size = int(input('Enter a board size from range<3, 5>: '))
            if 2 >= size or size > 5:
                print('You are trying to enter size from no acceptable range! Try again!')
        except ValueError:
            print('You entered not acceptable characters! Try again!')
    match size:
        case 3:
            board = [['*', '*', '*'], ['*', '*', '*'],['*', '*', '*']]
            return board
        case 4:
            board = [
                        ['*', '*', '*', '*'],
                        ['*', '*', '*', '*'],
                        ['*', '*', '*', '*'],
                        ['*', '*', '*', '*']
                    ]
            return board
        case 5:
            board = [
                        ['*', '*', '*', '*', '*'],
                        ['*', '*', '*', '*', '*'],
                        ['*', '*', '*', '*', '*'],
                        ['*', '*', '*', '*', '*'],
                        ['*', '*', '*', '*', '*']
                    ]
            return board
