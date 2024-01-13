import pygame
import sys
import random

# Initialize Pygame
pygame.init()

#game screen 
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("HerStory")
icon = pygame.image.load('classroom.jpeg')
pygame.display.set_icon(icon)

#fonts
mfont = pygame.font.SysFont(None, 100)



#Title 
# character display 
def player(x, y, playerImg):
    screen.blit(playerImg, (x, y))

def display_text(txt, font, colour, screen, xpos, ypos):
    text = font.render(txt, True, colour)
    #txtrec = txtobj.get_rect()
    #txtrec.topleft = (xpos, ypos)
    screen.blit(text, (xpos, ypos))

def mainDisplay():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False

        screen.fill((0, 0, 0))
        display_text('Herstory', mfont, (255, 255, 255), screen, 490, 200)
        pygame.display.update()

mainDisplay()
pygame.quit()
sys.exit()