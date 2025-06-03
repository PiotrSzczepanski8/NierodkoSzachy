class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.selected = False
        self.has_moved = False

    def check_movement(self, i, j, k, l):
        down_factor = i-j
        up_factor = i+j
        
        diagonal = straight = lshape = adjacent = forward = backwards = False
        
        if (k-l == down_factor) or (k+l == up_factor):
            diagonal = True

        if k == i or l == j:
            straight = True

        lshape_offsets = [(-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1)]
        if (k - i, l - j) in lshape_offsets:
            lshape = True
        
        if abs(i - k) <= 1 and abs(j - l) <= 1 and not (i == k and j == l):
            adjacent = True # king movement
        
        if self.color == 'white':
            if k == i - 1 and l == j:
                forward = True
            if i == 6 and k == i - 2 and l == j:
                forward = True
                
        elif self.color == 'black':
            if k == i + 1 and l == j:
                backwards = True
            if i == 1 and k == i + 2 and l == j:
                backwards = True

        if self.name == 'bishop' and diagonal == True:
            return True
        
        if self.name == 'rook' and straight == True:
            return True
        
        if self.name == 'queen' and (diagonal or straight):
            return True
        
        if self.name == 'knight' and lshape:
            return True
    
        if self.name == 'king' and adjacent:
            return True
        
        if self.name == 'pawn' and (forward or backwards):
            return True
        
        return False