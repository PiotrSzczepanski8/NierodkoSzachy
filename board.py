from piece import Piece
import numpy as np

class Board:
    def __init__(self):
        self.board = np.empty((8, 8),dtype=object)
        self.setup_pieces()

    def setup_pieces(self):
        self.board[7] = [
            Piece('rook', 'white'), Piece('knight', 'white'), Piece('bishop', 'white'),
            Piece('queen', 'white'), Piece('king', 'white'), Piece('bishop', 'white'),
            Piece('knight', 'white'), Piece('rook', 'white')
        ]
        self.board[6] = [Piece('pawn', 'white') for i in range(8)]

        self.board[0] = [
            Piece('rook', 'black'), Piece('knight', 'black'), Piece('bishop', 'black'),
            Piece('queen', 'black'), Piece('king', 'black'), Piece('bishop', 'black'),
            Piece('knight', 'black'), Piece('rook', 'black')
        ]
        self.board[1] = [Piece('pawn', 'black') for i in range(8)]

    # shortest way (i, j, k, l)