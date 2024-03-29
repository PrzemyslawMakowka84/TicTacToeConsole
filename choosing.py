
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
    match size:
        case 3:
            board = [['*', '*', '*'], ['*', '*', '*'] ,['*', '*', '*']]
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


def choosing_player():
    answer = input('Do you want play with computer?(y/n): ')
    while not (answer in ['y', 'n']) or (answer.isalpha() and len(answer) > 1):
        answer = input("Please type 'y' or 'n': ")
    match answer:
        case 'y':
            return True
        case 'n':
            return False
