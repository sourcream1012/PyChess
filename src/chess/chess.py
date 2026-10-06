import pygame
pygame.init()

class Chess:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.board

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