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
mfont = pygame.font.SysFont('georgia', 100)
# print(pygame.font.get_fonts())

# Create button
start_img = pygame.image.load("start.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (160, 160))
end_img = pygame.image.load("end_button.png").convert_alpha()
end_img = pygame.transform.scale(end_img, (160, 160))
rule_img = pygame.image.load("rule_button.png").convert_alpha()
rule_img = pygame.transform.scale(rule_img, (160, 160))

# Position of the button
start_button = Button(560, 210, start_img, 1)
end_button = Button(560, 310, end_img, 1)
rule_button = Button(560, 460, rule_img, 1)


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

                if rule_button.rect.collidepoint(event.pos):
                    print("Rules:")

            #screen = pygame.display.set_mode((1280, 720))
            background_img2 = pygame.image.load("schoolImage.png").convert()
            background_img2 = pygame.transform.scale(background_img2, (1280, 720))
            screen.blit(background_img2, (0, 0))
            display_text('Herstory', mfont, (248, 131, 121), screen, 450, 100)

            # Draw the button
            start_button.draw(screen)
            end_button.draw(screen)
            rule_button.draw(screen)

        pygame.display.update()

def draw_main_screen(screen):

    #game_screen1 = pygame.display.set_mode((1280, 720))
    background_img2 = pygame.image.load("schoolImage.png").convert()
    background_img2 = pygame.transform.scale(background_img2, (1280, 720))
    screen.blit(background_img2, (0, 0))

    display_text('Herstory', mfont, (248, 131, 121), screen, 450, 100)
    start_button.draw(screen)
    end_button.draw(screen)
    pygame.display.flip()


def move_avatar(screen, avatar, start_pos, end_pos, task_1):
    clock = pygame.time.Clock()
    x, y = start_pos
    target_x, target_y = end_pos
    speed = 5  # Adjust the speed as needed
    avatar_x = 100




    while x < 600:
        clock.tick(30)  # Limit the frame rate to 30 FPS

        x += speed
        # Define task_1 outside the startGame function
        screen.blit(task_1, (0, 0))  # Draw the task background
        screen.blit(avatar, (x, y))  # Draw the avatar at its new position
        pygame.display.flip()

def startGame():
    print("hello")

    game_screen = pygame.display.set_mode((1280, 720))
    background_img = pygame.image.load("classroom.jpeg").convert()
    background_img = pygame.transform.scale(background_img, (1280, 720))

    # character 1 (Ada Lovelace - wrote first computer program algorithm)
    main_avatar = pygame.image.load("avatar.png").convert_alpha()
    main_avatar = pygame.transform.scale(main_avatar, (100, 400))
    #character 2 (Tun Youyou - Chinese pharmacist who discovered arteminsen which is used to treat malaria)
    
    task_1 = pygame.image.load("task1.png").convert_alpha()
    task_1 = pygame.transform.scale(task_1, (1280, 720))
    main_avatar_smaller = pygame.transform.scale(main_avatar, (100, 200))

    #character 3 (Sally Ride - American women first women to travel to space)
    #third_avatar = pygame.image.load("").convert_alpha()
    #third_avatar = pygame.transform.scale(third_avatar, (100,400))

    #map 
    map = pygame.image.load("map.png").convert_alpha()
    map = pygame.transform.scale(map, (500, 700))


    font = pygame.font.SysFont(None, 36)

    message_index = 0
    messages = [
        "Welcome to HerStory! Your mission is to find the treasure chest at the end of the map <enter space>",
        "Here's your map. You have three tasks to complete in order to win.",
        "Your first task is to get over the bridge. You have three helpers. To learn more about them press space",
        "Opps, you need help! The bridge is broken."
    ]

    running = True
    avatar_display = False # track if avatar is shown
    map_display = False 
    task_display = False
    avatar_x = 100
    avatar_moved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                message_index += 1
                if message_index >= len(messages):
                    running = False
                if message_index==1:
                    avatar_display = True
                    map_display = True
                if message_index ==2:
                    task_display = True


        game_screen.blit(background_img, (0, 0))

        # Create a white box surface
        box_width, box_height = 1280, 200
        box_surface = pygame.Surface((box_width, box_height))
        box_surface.fill((255, 255, 255))
        box_rect = box_surface.get_rect(topleft=(0, 600))

        # Blit the white box onto the game screen
        game_screen.blit(box_surface, box_rect)

        # Create a text surface
        text_surface = font.render(messages[message_index], True, (0, 0, 0))  # Black text on white background

        # Center the text within the white box
        text_rect = text_surface.get_rect(center=box_rect.center)

        # Blit the text onto the game screen
        game_screen.blit(text_surface, text_rect)

        if avatar_display and map_display:
            game_screen.blit(main_avatar, (100, 200))
            game_screen.blit(map, (400, 0))

        
        if task_display: 
            game_screen.blit(task_1, (0,0))
            #TODO:add character to slide into the task_1 frame
            move_avatar(game_screen, main_avatar_smaller, (400, 175), (0, 0), task_1)  # Slide avatar to new position  


    

        pygame.display.flip()

    pygame.quit()
    sys.exit()

mainDisplay()
pygame.quit()
sys.exit()