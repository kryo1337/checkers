import pygame
import os


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
PADDING = 20
OUTLINE = 2

FPS = 60

PURPLE = (190, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (85, 85, 85)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(ROOT_DIR)
IMAGE_DIR = os.path.join(PROJECT_DIR, 'images')
IMAGE_PATH = os.path.join(IMAGE_DIR, 'crown.png')

CROWN = pygame.transform.scale(pygame.image.load(IMAGE_PATH), (45, 25))


