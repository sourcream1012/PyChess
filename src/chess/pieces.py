class Pieces:
    # Pieces class stores all of the game's pieces
    def __init__(self):
        pass

class Piece:
    # Piece class represents a single chess piece
    def __init__(self, type, color, position):
        self.type = type
        self.color = color
        self.position = position

# Eventually I'll add methods for each piece to define their movement rules which are then checked by the Chess class inside of chess.py which acts as the "server" for the chess game
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__("pawn", color, position)

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__("rook", color, position)

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__("knight", color, position)

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__("bishop", color, position)

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__("queen", color, position)

class King(Piece):
    def __init__(self, color, position):
        super().__init__("king", color, position)