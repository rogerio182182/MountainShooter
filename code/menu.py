import pygame.image

from code.cost import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Surface:
    pass


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text( 20,"Mountain",COLOR_ORANGE,((WIN_WIDTH / 2), 30))
            self.menu_text(20, "Shooter", COLOR_ORANGE , ((WIN_WIDTH / 2), 50))

            for i in range(len(MENU_OPTION)):
                self.menu_text(8, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 70 + 20 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
