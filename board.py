from piece import Piece
import numpy as np

class Board:
    def __init__(self):
        self.board = np.empty((8, 8),dtype=object)
        self.setup_pieces()
        self.rotated = False

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
    
    def no_collision(self, i, j, k, l):
        x, y = i, j

        dx = 1 if k > i else (-1 if k < i else 0)
        dy = 1 if l > j else (-1 if l < j else 0)

        while True:
            x += dx
            y += dy
            if (x, y) == (k, l):
                break
            if self.board[x][y] != None:
                return False

        return True
