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
exitbutton = pygame.image.load(os.path.join(image_path, "exit.png"))
menubar = pygame.image.load(os.path.join(image_path, "menuBar.png"))
startbutton_rect = startbutton.get_rect()
startbutton_rect.top = 200
startbutton_rect.left = 40
quitbutton_rect = quitbutton.get_rect()
quitbutton_rect.top = 330
quitbutton_rect.left = 40
exitbutton_rect = exitbutton.get_rect()
exitbutton_rect.top = 5
exitbutton_rect.left = 5
game_screen = False
pygame.mixer.music.load(os.path.join(music_path,"introMusic.wav"))
pygame.mixer.music.play()
intro = True 
backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))

def start_game():
    global game_screen
    backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))
    backbutton_rect = backbutton.get_rect()
    backbutton_rect.top = 5
    backbutton_rect.left = 5
    if game_screen:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join(music_path,"gameMusic.wav"))
        pygame.mixer.music.play()
    while game_screen:        
        background = pygame.image.load(os.path.join(image_path, "mainScreen.jpg"))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbuttonEntered.png"))
                if not backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))
        screen.blit(background, (0,0))
        screen.blit(backbutton, (5,5))

#   event loop

def game_menu():
    global intro
    global game_screen
    while intro:
        
        dt = clock.tick(60) #frame per second

        # 2. Event handling (keyboard, mouse, etc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user click the close button
                intro = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if startbutton_rect.collidepoint(pos):
                    startbutton = pygame.image.load(os.path.join(image_path, "startbuttonEntered.png"))

                if quitbutton_rect.collidepoint(pos):
                    quitbutton = pygame.image.load(os.path.join(image_path, "quitbuttonEntered.png"))

                if not startbutton_rect.collidepoint(pos):
                    startbutton = pygame.image.load(os.path.join(image_path, "startbutton.png"))

                if not quitbutton_rect.collidepoint(pos):
                    quitbutton = pygame.image.load(os.path.join(image_path, "quitbutton.png"))
                
                if exitbutton_rect.collidepoint(pos):
                    exitbutton = pygame.image.load(os.path.join(image_path, "exitEntered.png"))
                if not exitbutton_rect.collidepoint(pos):
                    exitbutton = pygame.image.load(os.path.join(image_path, "exit.png"))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #when user clicks 
                pos = pygame.mouse.get_pos()
                
                if exitbutton_rect.collidepoint(pos):
                    intro = False
                if startbutton_rect.collidepoint(pos):
                    game_screen = True
                    #background = pygame.image.load(os.path.join(image_path, "mainScreen.jpg"))
                    intro = False
                if quitbutton_rect.collidepoint(pos):
                    intro = False
                    break


        # 3. Character location
        # 4. Collision handling
        
        # 5. Display it in window
        screen.blit(background, (0, 0))
        screen.blit(startbutton, (40, 200))
        screen.blit(quitbutton, (40, 330))
        screen.blit(exitbutton, (5, 5))

        
        

        pygame.display.update()
    
game_menu()
start_game()

pygame.quit()