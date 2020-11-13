import os
import pygame
from graphic import Notebar
from graphic import Path
#############################################
#   Screen measurement
pygame.init() # reset 
#   initialize the window
screen_width = 1280 # x-axis
screen_height = 720 # y-axis
screen = pygame.display.set_mode((screen_width, screen_height))

#   Title 
pygame.display.set_caption("Rhythm Game")

#   FPS
clock = pygame.time.Clock()

#############################################
current_path = os.path.dirname(__file__)    # current file path
image_path = os.path.join(current_path, "images")
music_path = os.path.join(current_path, "music")

#   Background 
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
pygame.mixer.music.load(os.path.join(music_path,"introMusic.wav"))
pygame.mixer.music.play()
intro = True 
backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))
backbutton_rect = backbutton.get_rect()
backbutton_rect.top = 5
backbutton_rect.left = 5
black = (0,0,0)
white = (255, 255, 255)

def display_text(message, x, y, size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(message, True, color)
    screen.blit(text, (x,y))

#   Stops current music that is being played and start a new song with file name equals to parameter
def music_change(music):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, music + ".wav"))
    pygame.mixer.music.play()

def point(location):
    judge = 580
    pos = abs(location)
    result = ""
    percent = float(pos / judge)
    print(percent)
    if percent >= 0.99 and percent <= 1.01:
        return "Perfect"
    elif percent <= 1.03 and percent >= 0.97:
        return "Great"
    elif percent <= 1.035 and percent >= 0.965:
        return "Good"
    elif percent <= 1.05 and percent >= 0.95:
        return "Okay"
    return "Miss"

## input: judge_line judgementline
def evaluate(path, note):
    judgementline = pygame.image.load(os.path.join(image_path, "judgementline.png"))
    result = ""
    note_rect = note.get_image().get_rect()
    note_rect.top = note.get_y()
    note_rect.left = note.get_x()


    judge_line_rect = judgementline.get_rect()
    judge_line_rect.top = 580
    judge_line_rect.left = 0
    result = point(note.get_y())
    return result

#   Game play screen
def gameplay(level):
    global backbutton
    note_speed = 2
    sleep_time = 10
    reach_timme = 2
    gameplay = True
    title = pygame.image.load(os.path.join(image_path, "easyTitle.jpg"))
    judgementline = pygame.image.load(os.path.join(image_path, "judgementline.png"))
    hitbar = pygame.image.load(os.path.join(image_path, "hitbar.png"))
    barpathline = pygame.image.load(os.path.join(image_path, "barpathline.png"))
    s_path = Path(228)
    d_path = Path(332)
    f_path = Path(436)
    j_path = Path(744)
    k_path = Path(848)
    l_path = Path(952)
    space_path1 = Path(540)
    space_path2 = Path(640)
    s_bar = Notebar(228)
    d_bar = Notebar(332)
    f_bar = Notebar(436)
    j_bar = Notebar(744)
    k_bar = Notebar(848)
    l_bar = Notebar(952) 
    space_bar1 = Notebar(540)
    space_bar2 = Notebar(640)
    easy_bpm = 98
    medium_bpm = 148
    hard_bpm = 110
    notes = [s_bar, d_bar, f_bar, j_bar, k_bar, l_bar, space_bar1, space_bar2]
    start_time = 1000
    
    score_txt = "0"
    score = int(score_txt)

    screen.blit(background, (0,0))

    #   If user clicks easy
    if level == "easy":
        music_change("easyMusic")
        display_text("Hep you out - Leonel Cassio", 18, 675, 30, (255,255,255))
        display_text("Easy", 1200, 675, 30, (255,255,255))
        
        
        

    elif level == "medium":
        music_change("mediumMusic")
        title = pygame.image.load(os.path.join(image_path, "mediumTitle.jpg"))
        display_text("Sun goes down - Roy Knox", 18, 675, 30, (255,255,255))
        display_text("Medium", 1150, 675, 30, (255,255,255))
    else:
        music_change("hardMusic")
        title = pygame.image.load(os.path.join(image_path, "hardTitle.jpg"))
        display_text("Lioness - Dayfox", 18, 675, 30, (255,255,255))
        display_text("Hard", 1200, 675, 30, (255,255,255))

    while gameplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameplay = False
                music_change("gameMusic")

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbuttonEntered.png"))
                
                if not backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backbutton_rect.collidepoint(pos):
                    music_change("gameMusic")
                    gameplay = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: 
                    s_path.entered()
                    print(evaluate(s_path, s_bar))
                elif event.key == pygame.K_d:
                    d_path.entered()
                    print(evaluate(s_path, d_bar))
                elif event.key == pygame.K_f:
                    f_path.entered()
                    print(evaluate(s_path, f_bar))
                elif event.key == pygame.K_j:
                    j_path.entered()
                    print(evaluate(s_path, j_bar))
                elif event.key == pygame.K_k:
                    k_path.entered()
                    print(evaluate(s_path, k_bar))
                elif event.key == pygame.K_l:
                    l_path.entered()
                    print(evaluate(s_path, l_bar))
                elif event.key == pygame.K_SPACE:
                    space_path1.entered()
                    space_path2.entered()
                    print(evaluate(s_path, space_bar1))
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s: 
                    s_path.default()
                elif event.key == pygame.K_d:
                    d_path.default()
                elif event.key == pygame.K_f:
                    f_path.default()
                elif event.key == pygame.K_j:
                    j_path.default()
                elif event.key == pygame.K_k:
                    k_path.default()
                elif event.key == pygame.K_l:
                    l_path.default()
                elif event.key == pygame.K_SPACE:
                    space_path1.default()
                    space_path2.default()

        screen.blit(backbutton, (5,5))
        screen.blit(title, (340, 100))
        screen.blit(s_path.get_image(), (228,30))
        screen.blit(d_path.get_image(), (332,30))
        screen.blit(f_path.get_image(), (436,30))
        screen.blit(space_path1.get_image(), (540,30))
        screen.blit(space_path2.get_image(), (640,30))
        screen.blit(j_path.get_image(), (744,30))
        screen.blit(k_path.get_image(), (848,30))
        screen.blit(l_path.get_image(), (952,30))
        screen.blit(barpathline, (224,30))
        screen.blit(barpathline, (328,30))
        screen.blit(barpathline, (432,30))
        screen.blit(barpathline, (536,30))
        screen.blit(barpathline, (740,30))
        screen.blit(barpathline, (844,30))
        screen.blit(barpathline, (948,30))
        screen.blit(barpathline, (1052,30))
        screen.blit(judgementline, (0,580))
        screen.blit(hitbar, (0,660))

        for note in notes:
            note.set_y(note.get_y() + note_speed)
            if note.get_y() >= 620:  #   when it hits hitbar, location of hitbar - height of notebar
                note.default()  #   set notebar to default y position; which is -40
            screen.blit(note.get_image(), (note.get_x(), note.get_y()))

        display_text("S", 270, 586, 30, black)
        display_text("D", 374, 586, 30, black)
        display_text("F", 478, 586, 30, black)
        display_text("Space Bar", 570, 586, 30, black)
        display_text("J", 784, 586, 30, black)
        display_text("K", 889, 586, 30, black)
        display_text("L", 993, 586, 30, black)
        display_text(score_txt, 640, 675, 30, (255,255,255))
        pygame.display.update()
        
#   Game screen when user clicks start game button
def start_game():
    game_screen = True
    global backbutton
    background = pygame.image.load(os.path.join(image_path, "mainScreen.jpg"))
    easybutton = pygame.image.load(os.path.join(image_path, "easybutton.png"))
    mediumbutton = pygame.image.load(os.path.join(image_path, "mediumbutton.png"))
    hardbutton = pygame.image.load(os.path.join(image_path, "hardbutton.png"))
    easybutton_rect = easybutton.get_rect()
    easybutton_rect.top = 100
    easybutton_rect.left = 120
    mediumbutton_rect = mediumbutton.get_rect()
    mediumbutton_rect.top = 300
    mediumbutton_rect.left = 120
    hardbutton_rect = hardbutton.get_rect()
    hardbutton_rect.top = 500
    hardbutton_rect.left = 120
    music_change("gameMusic")

    while game_screen:        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbuttonEntered.png"))
                
                if not backbutton_rect.collidepoint(pos):
                    backbutton = pygame.image.load(os.path.join(image_path, "backbutton.png"))

                if easybutton_rect.collidepoint(pos):
                    easybutton = pygame.image.load(os.path.join(image_path, "easybuttonEntered.png"))
                if not easybutton_rect.collidepoint(pos):
                    easybutton = pygame.image.load(os.path.join(image_path, "easybutton.png"))

                if mediumbutton_rect.collidepoint(pos):
                    mediumbutton = pygame.image.load(os.path.join(image_path, "mediumbuttonEntered.png"))
                if not mediumbutton_rect.collidepoint(pos):
                    mediumbutton = pygame.image.load(os.path.join(image_path, "mediumbutton.png"))    
            
                if hardbutton_rect.collidepoint(pos):
                    hardbutton = pygame.image.load(os.path.join(image_path, "hardbuttonEntered.png"))
                if not hardbutton_rect.collidepoint(pos):
                    hardbutton = pygame.image.load(os.path.join(image_path, "hardbutton.png"))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if backbutton_rect.collidepoint(pos):
                    game_screen = False
                    music_change("introMusic")
                if easybutton_rect.collidepoint(pos):
                    gameplay("easy")
                if mediumbutton_rect.collidepoint(pos):
                    gameplay("medium")
                if hardbutton_rect.collidepoint(pos):
                    gameplay("hard")

        screen.blit(background, (0,0))
        screen.blit(backbutton, (5,5))
        screen.blit(easybutton, (120, 100))
        screen.blit(mediumbutton, (120, 300))
        screen.blit(hardbutton, (120, 500))
        pygame.display.update()

#   First screen when this game is played
def game_menu():
    global intro
    global startbutton
    global quitbutton
    global exitbutton
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
                    start_game()
                if quitbutton_rect.collidepoint(pos):
                    intro = False
                    break

        # 5. Display it in window
        screen.blit(background, (0, 0))
        screen.blit(startbutton, (40, 200))
        screen.blit(quitbutton, (40, 330))
        screen.blit(exitbutton, (5, 5))

        pygame.display.update()
    
game_menu()

pygame.quit()