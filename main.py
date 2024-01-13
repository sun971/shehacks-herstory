import pygame
import sys

# Define the Button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(pos) and not self.clicked:
                    self.clicked = True
                    action = True

        surface.blit(self.image, self.rect.topleft)

        return action

# Initialize Pygame
pygame.init()

# Game screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("HerStory")
icon = pygame.image.load('classroom.jpeg')
pygame.display.set_icon(icon)

# Fonts
mfont = pygame.font.SysFont(None, 100)

# Create button
start_img = pygame.image.load("start.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (400, 200))
end_img = pygame.image.load("end_button.png").convert_alpha()
end_img = pygame.transform.scale(end_img, (400, 200))

# Position of the button
start_button = Button(450, 300, start_img, 1)
end_button = Button(450, 400, end_img, 1)

def display_text(txt, font, colour, screen, xpos, ypos):
    text = font.render(txt, True, colour)
    screen.blit(text, (xpos, ypos))

def mainDisplay():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.KEYDOWN:
                status = False  # Handle other key events if needed
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check button click
                if start_button.rect.collidepoint(event.pos):
                    startGame()
                if end_button.rect.collidepoint(event.pos):
                    print("Button clicked!")
                    status = False  # Exit the loop when the button is clicked

        screen.fill((0, 0, 0))
        display_text('Herstory', mfont, (255, 255, 255), screen, 490, 200)

        # Draw the button
        start_button.draw(screen)
        end_button.draw(screen)

        pygame.display.update()

def startGame():
    print("hello")

mainDisplay()
pygame.quit()
sys.exit()