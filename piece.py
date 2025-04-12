class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def check_movement(self, i, j, k, l):
        down_factor = i-j
        up_factor = i+j
        if k-l == down_factor and k+l == up_factor:
            diagonal = True

        if k == i or l == j:
            straight = True

        offsets = [(-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1)]
        if [k - i, l - j] in offsets:
            lshape = True
        
        if abs(i - k) <= 1 and abs(j - l) <= 1 and not (i == k and j == l):
            adjacent = True

        if (i-1 == k or (i == 6 and k == 4)) and self.color == 'white':
            forward = True

        if (i+1 == k or (i == 1 and k == 3)) and self.color == 'black':
            backwards = True

        if self.name == 'bishop' and diagonal == True:
            return True
        
        if self.name == 'rook' and straight == True:
            return True
        
        if self.name == 'queen' and diagonal and straight:
            return True
        
        if self.name == 'knight' and lshape:
            return True
    
        if self.name == 'king' and adjacent:
            return True
        
        if self.name == 'pawn' and (forward or backwards):
            return True
        
        return False