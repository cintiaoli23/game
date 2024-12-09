import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = pygame.Rect(400, 300, 50, 50)  # Quadrado representando o jogador
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 255))  # Fundo azul
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)  # Jogador vermelho
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "menu"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "menu"  # Volta ao menu

            # Movimentação do jogador
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.y -= 5
            if keys[pygame.K_DOWN]:
                self.player.y += 5
            if keys[pygame.K_LEFT]:
                self.player.x -= 5
            if keys[pygame.K_RIGHT]:
                self.player.x += 5

            self.draw()
