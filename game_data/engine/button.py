import pygame
from enum import Enum





class Button:
    def __init__(self,
                 should_create_text: bool = True,
                 should_create_background: bool = False,
                 text: str = "",
                 text_size: int = 18,
                 text_color=(233, 233, 233, 255),
                 text_hover_color=(255, 255, 255, 255),
                 position = (0, 0),
                 background_color=(127, 127, 127, 255),
                 background_hover_color=(177, 177, 177, 255),
                 background_size = (100, 100),
                 owner: object = None,
                 custom_data = None):

        self.arguments_passed = [should_create_text,
                                 should_create_background,
                                 text,
                                 text_size,
                                 text_color,
                                 text_hover_color,
                                 position,
                                 background_color,
                                 background_hover_color,
                                 background_size]
        self.owner = owner
        self.text = None
        self.text_pos = ()
        self.background = None
        self.background_color = ()
        self.background_pos = ()
        self.custom_data = custom_data
        self.setup(should_create_text,
                   should_create_background,
                   text,
                   text_size,
                   text_color,
                   text_hover_color,
                   position,
                   background_color,
                   background_hover_color,
                   background_size)

    def setup(self,
              should_create_text: bool = True,
              should_create_background: bool = False,
              text: str = "",
              text_size: int = 18,
              text_color=(233, 233, 233, 255),
              text_hover_color=(255, 255, 255, 255),
              position = (0, 0),
              background_color=(127, 127, 127, 255),
              background_hover_color=(177, 177, 177, 255),
              background_size = (100, 100)):

        if should_create_text:
            self.text = pygame.font.SysFont('arial', text_size).render(text, True, text_color)
        if should_create_background:
            self.background_pos = position

            if should_create_text:
                size = (self.text.get_rect().width + 10, self.text.get_rect().height + 5)
                self.background = pygame.surface.Surface(size)
                self.text_pos = [
                    (self.background_pos[0] + self.background.get_rect().width / 2) - self.text.get_rect().width / 2,
                    (self.background_pos[1] + self.background.get_rect().height / 2) - self.text.get_rect().height / 2]
            else:
                self.background = pygame.surface.Surface(background_size)
            self.background_color = background_color
        elif should_create_text:
            self.text_pos = position

    def get_rect(self):
        if self.text is not None and self.background is None:
            return self.text.get_rect(center=self.text_pos)
        elif self.text is None and self.background is not None:
            return self.background.get_rect(center=self.background_pos)
        elif self.text is not None and self.background is not None:
            return self.background.get_rect(center=self.background_pos)
        return pygame.Rect(0, 0, 0, 0)

    def draw(self, renderer: pygame.surface.Surface):
        if self.background is not None:
            self.background.fill(self.background_color)
            renderer.blit(self.background, self.background.get_rect(center=self.background_pos))
        if self.text is not None:
            if self.background is not None:
                renderer.blit(self.text, self.text.get_rect(center=self.background_pos))
            else:
                renderer.blit(self.text, self.text.get_rect(center=self.text_pos))

    def handle_event(self, event: ButtonEvent, mouse_pos):
        if self.background.get_rect(center=self.background_pos).collidepoint(mouse_pos):
            if event == ButtonEvent.Hover:
                self.on_hover()
            if event == ButtonEvent.Click:
                self.on_click()
        else:
            self.on_unhover()

    def on_hover(self):
        self.text = pygame.font.SysFont('arial', self.arguments_passed[3]).render(self.arguments_passed[2], True, self.arguments_passed[5])
        self.background_color = self.arguments_passed[8]
        pass

    def on_unhover(self):
        self.text = pygame.font.SysFont('arial', self.arguments_passed[3]).render(self.arguments_passed[2], True, self.arguments_passed[4])
        self.background_color = self.arguments_passed[7]

    def on_click(self):
        pass


