import pygame
from pathlib import Path
from pieces import Pieces
from pieces import Piece

pygame.init()

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent.parent
BLACK_IMG_DIR = ROOT / "assets" / "img" / "black"
WHITE_IMG_DIR = ROOT / "assets" / "img" / "White"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOARD_WIDTH = 800
BOARD_HEIGHT = 800

BACKGROUND_COLOR = (181, 136, 99)

TILE_SIZE = BOARD_WIDTH // 8

class Board:
    # Board class handles initiating the chess board and handling piece movement not logic though
    def __init__(self):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.pieces = Pieces()

    def init_board_pieces(self) -> None:
        self.pieces.init_pieces()
        for piece in self.pieces.pieces:
            x, y = piece.position
            self.grid[x][y] = piece

    def draw_board(self, screen: pygame.Surface) -> None:
        for y in range(8):
            for x in range(8):
                color = (240, 217, 181) if (x + y) % 2 == 0 else (BACKGROUND_COLOR)
                pygame.draw.rect(
                    screen, 
                    color, 
                    (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )
                piece = self.grid[x][y]
                if piece:
                    img_path = None

                    if piece.team == "black":
                        img_path = BLACK_IMG_DIR / f"{piece.team}_{piece.type}.png"
                    else:
                        img_path = WHITE_IMG_DIR / f"{piece.team}_{piece.type}.png"

                    image = pygame.image.load(img_path)
                    screen.blit(
                        image, 
                        (x * TILE_SIZE, y * TILE_SIZE),
                        (0, 0, image.get_width(), image.get_height())
                    )

    def get_white_pieces(self) -> list:
        white_pieces = []
        for piece in self.pieces.pieces:
            if piece.team == "white":
                white_pieces.append(piece)
        return white_pieces

    def get_black_pieces(self) -> list:
        black_pieces = []
        for piece in self.pieces.pieces:
            if piece.team == "black":
                black_pieces.append(piece)
        return black_pieces

    def move_piece(self, piece: Piece, new_x: int, new_y: int) -> None:
        old_x, old_y = piece.position
        self.grid[old_x][old_y] = 0
        self.grid[new_x][new_y] = piece
        piece.position = (new_x, new_y)

    def piece_is_on_tile(self, x: int, y: int) -> bool:
        if self.grid[x][y]:
            return True
        return False

    def get_piece_on_tile(self, x: int, y: int) -> object:
        if self.grid[x][y] == 0: return None
        return self.grid[x][y]

    def highlight_selected_piece(self, screen: pygame.Surface, selectedPiece: Piece) -> None:
        x, y = selectedPiece.position
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            2
        )

    def __str__(self) -> str:
        board_str = ""
        for y in range(8):
            for x in range(8):
                piece = self.grid[x][y]
                if piece:
                    board_str += f"{piece.type[0].upper() if piece.team == 'white' else piece.type[0].lower()} "
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str

class Chess:
    # Chess class represents the main game and handles the game loop, rendering, and the game state management
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.your_team = "white"

        self.board = Board()
        self.board.init_board_pieces()

        self.selected_piece = None
        self.pieces = {
            "white": self.board.get_white_pieces(),
            "black": self.board.get_black_pieces()
        }

    def start(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    col = x // TILE_SIZE
                    row = y // TILE_SIZE

                    # Checks if you already have a selected piece to see if you can move it
                    if self.selected_piece != None:
                        possible_moves = self.selected_piece.possible_moves(self.pieces[self.your_team])
                        if (col, row) in possible_moves:
                            self.board.move_piece(self.selected_piece, col, row)
                            self.selected_piece = None
                            continue

                    self.selected_piece = self.board.get_piece_on_tile(col, row)

                    # Checks if there is a piece on the clicked tile
                    if not self.selected_piece:
                        print(
                            f"Clicked on tile ({col}, {row})\n"
                            f"Piece on tile: {self.board.piece_is_on_tile(col, row)}\n"
                            f"Piece details: no piece on tile\n"
                        )
                        continue

                    # If the selected piece is not on your team it unselects it
                    if self.selected_piece.team != self.your_team:
                        self.selected_piece = None
                        continue
                    
                    print(
                        f"Clicked on tile ({col}, {row})\n"
                        f"Piece on tile: {self.board.piece_is_on_tile(col, row)}\n"
                        f"Piece details: {self.selected_piece}\n"
                    )
                    

            self.screen.fill(BACKGROUND_COLOR)

            self.board.draw_board(self.screen)

            if self.selected_piece:
                self.board.highlight_selected_piece(self.screen, self.selected_piece)
           
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Chess()
    game.start()