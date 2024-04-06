from Board import Board


is_computer_play = Board.choosing_player()
size = Board.choose_size_board()
board = Board(size, is_computer_play)
board.play()
