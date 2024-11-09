import pygame
pygame.init()

clock = pygame.time.Clock()

display_suface= pygame.display.set_mode((500, 500))

pygame.display.set_caption('image')

image = pygame.image.load('image.jpg')

DEFAULT_IMAGE_SIZE = (200, 200)

image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)