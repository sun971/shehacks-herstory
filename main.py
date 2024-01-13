import pygame
import sys
from button import Button

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


# Create button
start_img = pygame.image.load("start.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (400, 200))
end_img = pygame.image.load("end_button.png").convert_alpha()
end_img = pygame.transform.scale(end_img, (400, 200))

#position of the button
start_button = Button(450, 300, start_img, 1)
end_button = Button(450, 400, end_img, 1)


def mainDisplay():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False

        screen.fill((0, 0, 0))
        display_text('Herstory', mfont, (255, 255, 255), screen, 490, 200)

        # Draw the button
        start_button.draw(screen)
        end_button.draw(screen)


        pygame.display.update()

mainDisplay()
pygame.quit()
sys.exit()