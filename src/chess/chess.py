import pygame
from pieces import Pieces

pygame.init()

class Board:
    # Board class handles initiating the chess board and handling piece movement not logic though
    def __init__(self):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.pieces = Pieces()

    def init_board_pieces(self):
        self.pieces.init_pieces()
        for piece in self.pieces.pieces:
            x, y = piece.position
            self.grid[x][y] = piece

class Chess:
    # Chess class represents the main game and handles the game loop, rendering, and the game state management
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.board = Board()
        self.board.init_board_pieces()

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