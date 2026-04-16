import pygame

pygame.init()
#print(pygame.display.get_desktop_sizes())
screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    