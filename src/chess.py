import pygame
pygame.init()

# Piece-related constants
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

def piece_is_in_cell(Pieces: list[ChessPiece], x: int, y: int) -> tuple[bool, ChessPiece | int]:
    for piece in Pieces:
        if piece.x == x and piece.y == y:
            return True, piece
    return False, 0

def create_chess_grid() -> list[list[ChessPiece]]:
    grid = []
    Pieces = init_chess_pieces()
    Pieces = [piece for team in Pieces for piece in team]
    for y in range(8):
        row = []
        for x in range(8):
            row.append(piece_is_in_cell(Pieces, x, y)[1])
        grid.append(row)
    return grid

def init_chess_pieces() -> list[list[ChessPiece]]:
    pieces_white = []
    pieces_black = []

    for x, y, piece_type, team in BEGINNING_POSITIONS[0]:
        pieces_white.append(ChessPiece(x, y, piece_type, team))
    for x, y, piece_type, team in BEGINNING_POSITIONS[1]:
        pieces_black.append(ChessPiece(x, y, piece_type, team))

    return [pieces_white, pieces_black]

def print_chess_grid(grid: list[list[ChessPiece]]):
    for row in grid:
        print([f"{piece.piece_type}_{piece.team}({piece.x},{piece.y})" if piece else " " for piece in row])

class ChessPiece:
    def __init__(self, x: int, y: int, piece_type: str, team: str):
        self.x = x
        self.y = y
        self.piece_type = piece_type
        self.team = team

class Chess:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.grid = create_chess_grid()

    def start(self):
        print_chess_grid(self.grid)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
           
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Chess()
    game.start()