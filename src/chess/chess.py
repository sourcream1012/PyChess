import pygame
from pieces import Pieces

pygame.init()

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
                    # Will add the piece image later
                    continue

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
        self.board = Board()
        self.board.init_board_pieces()

    def start(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BACKGROUND_COLOR)

            self.board.draw_board(self.screen)
           
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Chess()
    game.start()