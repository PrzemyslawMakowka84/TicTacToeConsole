from Board import Board


def main():
    size = Board.choose_size_board()
    board = Board(size)
    board.play()


if __name__ == '__main__':
    main()
