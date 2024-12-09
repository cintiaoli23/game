import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)  # Fonte do texto
        self.options = ["Start Game", "Exit"]  # Opções do menu
        self.selected_index = 0  # Qual opção está selecionada

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fundo preto
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_index else (100, 100, 100)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(400, 300 + i * 60))
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_index] == "Start Game":
                            return "game"
                        elif self.options[self.selected_index] == "Exit":
                            return "exit"

            self.draw()
