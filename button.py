import pygame

class Button:
    def __init__(self, file_name, size=(0,0), position=(0,0)):
        self.surface = pygame.image.load(file_name)
        if size != (0,0):
            self.size = size
        else:
            self.size = self.surface.get_size()
        self.surface = pygame.transform.scale(self.surface, self.size)
        self.position = position
        self.rect = self.surface.get_rect().move(self.position[0], self.position[1])
        self.is_rendered = False

    def is_touching_mouse(self, mouse_pos):
        if self.is_rendered:
            return self.rect.collidepoint(mouse_pos)
        return False

    def render(self, screen):
        screen.blit(self.surface, self.position)
        self.is_rendered = True

    def unrender(self):
        self.is_rendered = False