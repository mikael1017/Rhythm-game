import os
import pygame
#############################################
#   Must have
pygame.init() # reset 
#   initialize the window
screen_width = 1280 # x-axis
screen_height = 720 # y-axis
screen = pygame.display.set_mode((screen_width, screen_height))

#   Title 
pygame.display.set_caption("Pang game")

#   FPS
clock = pygame.time.Clock()

#############################################

# 1. Background, Game image, Character, Position of image, Font
current_path = os.path.dirname(__file__)    # current file path
image_path = os.path.join(current_path, "images")
music_path = os.path.join(current_path, "music")

#   Background, Character, 
background = pygame.image.load(os.path.join(image_path, "background.jpg"))
startbutton = pygame.image.load(os.path.join(image_path, "startbutton.png"))
startbutton_over = "startbuttonEntered.png"
quitbutton_over = "quitbuttonEntered.png"
quitbutton = pygame.image.load(os.path.join(image_path, "quitbutton.png"))
startbutton = pygame.image.load(os.path.join(image_path, "startbutton.png"))
startbutton_rect = startbutton.get_rect()
startbutton_rect.top = 200
startbutton_rect.left = 40
quitbutton_rect = quitbutton.get_rect()
quitbutton_rect.top = 330
quitbutton_rect.left = 40
game_screen = False
pygame.mixer.music.load(os.path.join(music_path,"introMusic.wav"))
pygame.mixer.music.play()

def start_game():
    background = pygame.image.load(os.path.join(image_path, "mainScreen.jpg"))
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path,"gameMusic.wav"))
    pygame.mixer.music.play()
    

#   event loop
running = True 
while running:
    
    dt = clock.tick(60) #frame per second

    # 2. Event handling (keyboard, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user click the close button
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #when user clicks 
            pos = pygame.mouse.get_pos()
            print(pos);
            if startbutton_rect.collidepoint(pos):
                background = pygame.image.load(os.path.join(image_path, "mainScreen.jpg"))
                start_game()
            if quitbutton_rect.collidepoint(pos):
                running = False
                break


    # 3. Character location
    # 4. Collision handling
    
    # 5. Display it in window
    screen.blit(background, (0, 0))
    screen.blit(startbutton, (40, 200))
    screen.blit(quitbutton, (40, 330))

    
    

    pygame.display.update()


pygame.quit()