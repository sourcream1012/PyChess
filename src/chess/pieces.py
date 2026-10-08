PIECE_TYPES = ["king", "queen", "rook", "bishop", "knight", "pawn"]
MAX_NUM_EACH_PIECE = {
    PIECE_TYPES[0]: 1,
    PIECE_TYPES[1]: 1,
    PIECE_TYPES[2]: 2,
    PIECE_TYPES[3]: 2,
    PIECE_TYPES[4]: 2,
    PIECE_TYPES[5]: 8
}
BEGINNING_POSITIONS = [
    [ #black pieces
        [0, 0, "rook", "black"],
        [1, 0, "knight", "black"],
        [2, 0, "bishop", "black"],
        [3, 0, "queen", "black"],
        [4, 0, "king", "black"],
        [5, 0, "bishop", "black"],
        [6, 0, "knight", "black"],
        [7, 0, "rook", "black"],
        # Black pawns
        [0, 1, "pawn", "black"],
        [1, 1, "pawn", "black"],
        [2, 1, "pawn", "black"],
        [3, 1, "pawn", "black"],
        [4, 1, "pawn", "black"],
        [5, 1, "pawn", "black"],
        [6, 1, "pawn", "black"],
        [7, 1, "pawn", "black"],
    ],
    [ #White pieces
        [0, 7, "rook", "white"],
        [1, 7, "knight", "white"],
        [2, 7, "bishop", "white"],
        [3, 7, "queen", "white"],
        [4, 7, "king", "white"],
        [5, 7, "bishop", "white"],
        [6, 7, "knight", "white"],
        [7, 7, "rook", "white"],
        # White pawns
        [0, 6, "pawn", "white"],
        [1, 6, "pawn", "white"],
        [2, 6, "pawn", "white"],
        [3, 6, "pawn", "white"],
        [4, 6, "pawn", "white"],
        [5, 6, "pawn", "white"],
        [6, 6, "pawn", "white"],
        [7, 6, "pawn", "white"],
    ]
]

class Pieces:
    # Pieces class stores all of the game's pieces
    def __init__(self):
        self.pieces = []

    def init_pieces(self):
        self.pieces = []
        for team_index, team_positions in enumerate(BEGINNING_POSITIONS):
            for x, y, piece_type, team in team_positions:
                self.pieces.append(Piece(piece_type, team, (x, y)))

class Piece:
    # Piece class represents a single chess piece
    def __init__(self, type, team, position):
        self.type = type
        self.team = team
        self.position = position

# Eventually I'll add methods for each piece to define their movement rules which are then checked by the Chess class inside of chess.py which acts as the "server" for the chess game
class Pawn(Piece):
    def __init__(self, team, position):
        super().__init__("pawn", team, position)

    def request_move(self):
        pass

class Rook(Piece):
    def __init__(self, team, position):
        super().__init__("rook", team, position)

    def request_move(self):
        pass

class Knight(Piece):
    def __init__(self, team, position):
        super().__init__("knight", team, position)

    def request_move(self):
        pass

class Bishop(Piece):
    def __init__(self, team, position):
        super().__init__("bishop", team, position)

    def request_move(self):
        pass

class Queen(Piece):
    def __init__(self, team, position):
        super().__init__("queen", team, position)

    def request_move(self):
        pass

class King(Piece):
    def __init__(self, team, position):
        super().__init__("king", team, position)

    def request_move(self):
        pass