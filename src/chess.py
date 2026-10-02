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

def piece_is_in_cell(Pieces: list[ChessPiece], x: int, y: int) -> tuple[bool, ChessPiece]:
    for piece in Pieces:
        if piece.x == x and piece.y == y:
            return True, piece
    return False, None

def create_chess_grid(Pieces: list[ChessPiece]) -> list[list[ChessPiece]]:
    grid = []
    for y in range(8):
        row = []
        for x in range(8):
            row.append(piece_is_in_cell(Pieces, x, y)[1])
        grid.append(row)
    return grid

def init_chess_pieces() -> list[ChessPiece]:
    pieces_white = []
    pieces_black = []

    for piece_type in PIECE_TYPES:
        for i in range(MAX_NUM_EACH_PIECE[piece_type]):
            pass

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

    def start(self):
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