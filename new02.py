import pygame

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Pong')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 30) 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
a = 90
print a