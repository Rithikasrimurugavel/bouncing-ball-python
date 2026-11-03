'''import pygame 
import time 
import random 
  
# initialize pygame and set the colors 
pygame.init() 
gray = (119, 118, 110) 
black = (0, 0, 0) 
red = (255, 0, 0) 
green = (0, 200, 0) 
blue = (0, 0, 200) 
bright_red = (255, 0, 0) 
bright_green = (0, 255, 0) 
bright_blue = (0, 0, 255) 
display_width = 800
display_height = 600
  
gamedisplays = pygame.display.set_mode( 
    (display_width, display_height)) 
pygame.display.set_caption("car game") 
clock = pygame.time.Clock() 
carimg = pygame.image.load('car1.jpg') 
backgroundpic = pygame.image.load("download12.jpg") 
yellow_strip = pygame.image.load("yellow strip.jpg") 
strip = pygame.image.load("strip.jpg") 
intro_background = pygame.image.load("background.jpg") 
instruction_background = pygame.image.load("background2.jpg") 
car_width = 56
pause = False
  
# Intro screen 
  
  
def intro_loop(): 
    intro = True
    while intro: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
                sys.exit() 
        gamedisplays.blit(intro_background, (0, 0)) 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("CAR GAME", largetext) 
        TextRect.center = (400, 100) 
        gamedisplays.blit(TextSurf, TextRect) 
        button("START", 150, 520, 100, 50, green, 
               bright_green, "play") 
        button("QUIT", 550, 520, 100, 
               50, 
               red, 
               bright_red, 
               "quit") 
        button("INSTRUCTION", 300, 520, 200, 
               50, blue, bright_blue, 
               "intro") 
        pygame.display.update() 
        clock.tick(50) 
  
  
def button(msg, x, y, w, h, ic, ac, action=None): 
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 
    if x+w > mouse[0] > x and y+h > mouse[1] > y: 
        pygame.draw.rect(gamedisplays, 
                         ac, (x, y, w, h)) 
        if click[0] == 1 and action != None: 
            if action == "play": 
                countdown() 
            elif action == "quit": 
                pygame.quit() 
                quit() 
                sys.exit() 
            elif action == "intro": 
                introduction() 
            elif action == "menu": 
                intro_loop() 
            elif action == "pause": 
                paused() 
            elif action == "unpause": 
                unpaused() 
  
    else: 
        pygame.draw.rect(gamedisplays, 
                         ic, 
                         (x, y, w, h)) 
    smalltext = pygame.font.Font("freesansbold.ttf", 20) 
    textsurf, textrect = text_objects(msg, smalltext) 
    textrect.center = ((x+(w/2)), (y+(h/2))) 
    gamedisplays.blit(textsurf, textrect) 
  
  
def introduction(): 
    introduction = True
    while introduction: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
                sys.exit() 
        gamedisplays.blit(instruction_background, (0, 0)) 
        largetext = pygame.font.Font('freesansbold.ttf', 80) 
        smalltext = pygame.font.Font('freesansbold.ttf', 20) 
        mediumtext = pygame.font.Font('freesansbold.ttf', 40) 
        textSurf, textRect = text_objects( 
            "This is an car game in which you" +
            "need dodge the coming cars", smalltext) 
        textRect.center = ((350), (200)) 
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext) 
        TextRect.center = ((400), (100)) 
        gamedisplays.blit(TextSurf, TextRect) 
        gamedisplays.blit(textSurf, textRect) 
        stextSurf, stextRect = text_objects( 
            "ARROW LEFT : LEFT TURN", smalltext) 
        stextRect.center = ((150), (400)) 
        hTextSurf, hTextRect = text_objects( 
            "ARROW RIGHT : RIGHT TURN", smalltext) 
        hTextRect.center = ((150), (450)) 
        atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext) 
        atextRect.center = ((150), (500)) 
        rtextSurf, rtextRect = text_objects("B : BRAKE ", smalltext) 
        rtextRect.center = ((150), (550)) 
        ptextSurf, ptextRect = text_objects("P : PAUSE  ", smalltext) 
        ptextRect.center = ((150), (350)) 
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext) 
        sTextRect.center = ((350), (300)) 
        gamedisplays.blit(sTextSurf, sTextRect) 
        gamedisplays.blit(stextSurf, stextRect) 
        gamedisplays.blit(hTextSurf, hTextRect) 
        gamedisplays.blit(atextSurf, atextRect) 
        gamedisplays.blit(rtextSurf, rtextRect) 
        gamedisplays.blit(ptextSurf, ptextRect) 
        button("BACK", 600, 450, 100, 50, blue, 
               bright_blue, "menu") 
        pygame.display.update() 
        clock.tick(30) 
  
  
def paused(): 
    global pause 
  
    while pause: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
                sys.exit() 
        gamedisplays.blit(instruction_background, (0, 0)) 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("PAUSED", largetext) 
        TextRect.center = ( 
            (display_width/2), 
            (display_height/2) 
        ) 
        gamedisplays.blit(TextSurf, TextRect) 
        button("CONTINUE", 150, 450, 
               150, 50, green, 
               bright_green, "unpause") 
        button("RESTART", 350, 450, 150, 
               50, blue, bright_blue, 
               "play") 
        button("MAIN MENU", 550, 450, 
               200, 50, red, bright_red, 
               "menu") 
        pygame.display.update() 
        clock.tick(30) 
  
  
def unpaused(): 
    global pause 
    pause = False
  
  
def countdown_background(): 
    font = pygame.font.SysFont(None, 25) 
    x = (display_width*0.45) 
    y = (display_height*0.8) 
    gamedisplays.blit(backgroundpic, (0, 0)) 
    gamedisplays.blit(backgroundpic, (0, 200)) 
    gamedisplays.blit(backgroundpic, (0, 400)) 
    gamedisplays.blit(backgroundpic, (700, 0)) 
    gamedisplays.blit(backgroundpic, (700, 200)) 
    gamedisplays.blit(backgroundpic, (700, 400)) 
    gamedisplays.blit(yellow_strip, (400, 100)) 
    gamedisplays.blit(yellow_strip, (400, 200)) 
    gamedisplays.blit(yellow_strip, (400, 300)) 
    gamedisplays.blit(yellow_strip, (400, 400)) 
    gamedisplays.blit(yellow_strip, (400, 100)) 
    gamedisplays.blit(yellow_strip, (400, 500)) 
    gamedisplays.blit(yellow_strip, (400, 0)) 
    gamedisplays.blit(yellow_strip, (400, 600)) 
    gamedisplays.blit(strip, (120, 200)) 
    gamedisplays.blit(strip, (120, 0)) 
    gamedisplays.blit(strip, (120, 100)) 
    gamedisplays.blit(strip, (680, 100)) 
    gamedisplays.blit(strip, (680, 0)) 
    gamedisplays.blit(strip, (680, 200)) 
    gamedisplays.blit(carimg, (x, y)) 
    text = font.render("DODGED: 0", True, black) 
    score = font.render("SCORE: 0", True, red) 
    gamedisplays.blit(text, (0, 50)) 
    gamedisplays.blit(score, (0, 30)) 
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause") 
  
  
def countdown(): 
    countdown = True
  
    while countdown: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
                sys.exit() 
        gamedisplays.fill(gray) 
        countdown_background() 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("3", largetext) 
        TextRect.center = ( 
            (display_width/2), 
            (display_height/2)) 
        gamedisplays.blit(TextSurf, TextRect) 
        pygame.display.update() 
        clock.tick(1) 
        gamedisplays.fill(gray) 
        countdown_background() 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("2", largetext) 
        TextRect.center = ( 
            (display_width/2), 
            (display_height/2)) 
        gamedisplays.blit(TextSurf, TextRect) 
        pygame.display.update() 
        clock.tick(1) 
        gamedisplays.fill(gray) 
        countdown_background() 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("1", largetext) 
        TextRect.center = ( 
            (display_width/2), 
            (display_height/2)) 
        gamedisplays.blit(TextSurf, TextRect) 
        pygame.display.update() 
        clock.tick(1) 
        gamedisplays.fill(gray) 
        countdown_background() 
        largetext = pygame.font.Font('freesansbold.ttf', 115) 
        TextSurf, TextRect = text_objects("GO!!!", largetext) 
        TextRect.center = ( 
            (display_width/2), 
            (display_height/2)) 
        gamedisplays.blit(TextSurf, TextRect) 
        pygame.display.update() 
        clock.tick(1) 
        game_loop() 
  
  
def obstacle(obs_startx, obs_starty, obs): 
    if obs == 0: 
        obs_pic = pygame.image.load("car.jpg") 
    elif obs == 1: 
        obs_pic = pygame.image.load("car1.jpg") 
    elif obs == 2: 
        obs_pic = pygame.image.load("car2.jpg") 
    elif obs == 3: 
        obs_pic = pygame.image.load("car4.jpg") 
    elif obs == 4: 
        obs_pic = pygame.image.load("car5.jpg") 
    elif obs == 5: 
        obs_pic = pygame.image.load("car6.jpg") 
    elif obs == 6: 
        obs_pic = pygame.image.load("car7.jpg") 
    gamedisplays.blit(obs_pic, 
                      (obs_startx, 
                       obs_starty)) 
  
  
def score_system(passed, score): 
    font = pygame.font.SysFont(None, 25) 
    text = font.render("Passed"+str(passed), True, black) 
    score = font.render("Score"+str(score), True, red) 
    gamedisplays.blit(text, (0, 50)) 
    gamedisplays.blit(score, (0, 30)) 
  
  
def text_objects(text, font): 
    textsurface = font.render(text, True, black) 
    return textsurface, textsurface.get_rect() 
  
  
def message_display(text): 
    largetext = pygame.font.Font("freesansbold.ttf", 80) 
    textsurf, textrect = text_objects(text, largetext) 
    textrect.center = ( 
        (display_width/2), 
        (display_height/2)) 
    gamedisplays.blit(textsurf, textrect) 
    pygame.display.update() 
    time.sleep(3) 
    game_loop() 
  
  
def crash(): 
    message_display("YOU CRASHED") 
  
  
def background(): 
    gamedisplays.blit(backgroundpic, (0, 0)) 
    gamedisplays.blit(backgroundpic, (0, 200)) 
    gamedisplays.blit(backgroundpic, (0, 400)) 
    gamedisplays.blit(backgroundpic, (700, 0)) 
    gamedisplays.blit(backgroundpic, (700, 200)) 
    gamedisplays.blit(backgroundpic, (700, 400)) 
    gamedisplays.blit(yellow_strip, (400, 0)) 
    gamedisplays.blit(yellow_strip, (400, 100)) 
    gamedisplays.blit(yellow_strip, (400, 200)) 
    gamedisplays.blit(yellow_strip, (400, 300)) 
    gamedisplays.blit(yellow_strip, (400, 400)) 
    gamedisplays.blit(yellow_strip, (400, 500)) 
    gamedisplays.blit(strip, (120, 0)) 
    gamedisplays.blit(strip, (120, 100)) 
    gamedisplays.blit(strip, (120, 200)) 
    gamedisplays.blit(strip, (680, 0)) 
    gamedisplays.blit(strip, (680, 100)) 
    gamedisplays.blit(strip, (680, 200)) 
  
  
def car(x, y): 
    gamedisplays.blit(carimg, (x, y)) 
  
  
def game_loop(): 
    global pause 
    x = (display_width*0.45) 
    y = (display_height*0.8) 
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, 
                                  (display_width-200)) 
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120
  
    bumped = False
    while not bumped: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
  
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    x_change = -5
                if event.key == pygame.K_RIGHT: 
                    x_change = 5
                if event.key == pygame.K_a: 
                    obstacle_speed += 2
                if event.key == pygame.K_b: 
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT: 
                    x_change = 0
                if event.key == pygame.K_RIGHT: 
                    x_change = 0
  
        x += x_change 
        pause = True
        gamedisplays.fill(gray) 
  
        rel_y = y2 % backgroundpic.get_rect().width 
        gamedisplays.blit( 
            backgroundpic, (0, 
                            rel_y-backgroundpic.get_rect().width)) 
        gamedisplays.blit(backgroundpic, 
                          (700, rel_y -
                           backgroundpic.get_rect().width)) 
        if rel_y < 800: 
            gamedisplays.blit(backgroundpic, (0, rel_y)) 
            gamedisplays.blit(backgroundpic, (700, rel_y)) 
            gamedisplays.blit(yellow_strip, (400, rel_y)) 
            gamedisplays.blit(yellow_strip, (400, rel_y+100)) 
            gamedisplays.blit(yellow_strip, (400, rel_y+200)) 
            gamedisplays.blit(yellow_strip, (400, rel_y+300)) 
            gamedisplays.blit(yellow_strip, (400, rel_y+400)) 
            gamedisplays.blit(yellow_strip, (400, rel_y+500)) 
            gamedisplays.blit(yellow_strip, (400, rel_y-100)) 
            gamedisplays.blit(strip, (120, rel_y-200)) 
            gamedisplays.blit(strip, (120, rel_y+20)) 
            gamedisplays.blit(strip, (120, rel_y+30)) 
            gamedisplays.blit(strip, (680, rel_y-100)) 
            gamedisplays.blit(strip, (680, rel_y+20)) 
            gamedisplays.blit(strip, (680, rel_y+30)) 
  
        y2 += obstacle_speed 
  
        obs_starty -= (obstacle_speed/4) 
        obstacle(obs_startx, obs_starty, obs) 
        obs_starty += obstacle_speed 
        car(x, y) 
        score_system(passed, score) 
        if x > 690-car_width or x < 110: 
            crash() 
        if x > display_width-(car_width+110) or x < 110: 
            crash() 
        if obs_starty > display_height: 
            obs_starty = 0-obs_height 
            obs_startx = random.randrange(170, 
                                          (display_width-170)) 
            obs = random.randrange(0, 7) 
            passed = passed+1
            score = passed*10
            if int(passed) % 10 == 0: 
                level = level+1
                obstacle_speed+2
                largetext = pygame.font.Font("freesansbold.ttf", 80) 
                textsurf, textrect = text_objects( 
                    "LEVEL"+str(level), largetext) 
                textrect.center = ( 
                    (display_width/2), (display_height/2)) 
                gamedisplays.blit(textsurf, textrect) 
                pygame.display.update() 
                time.sleep(3) 
  
                if y < obs_starty+obs_height: 
                    if (x > obs_startx and x <\obs_startx + obs_width or x+car_width > \ (obs_startx and x+car_width < obs_startx+obs_width)): 
                        crash() 
                button("Pause", 650, 0, 150, 50, blue, bright_blue, "pause") 
pygame.display.update() 
clock.tick(60) 
  
  
intro_loop() 
game_loop() 
pygame.quit() 
quit()'''
'''import pygame

# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Blossom Blast")

# Load the image
try:
    image = pygame.image.load(r'C:\rithika\pygame install\emoji.png')
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()

# Get the image dimensions
image_width, image_height = image.get_size()

# Initial position and velocity
x = 600
y = 600
vel = 10

run = True
while run:
    pygame.time.delay(10)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1000 - image_width:
        x += vel

    # Clear the screen
    win.fill((0, 0, 0))

    # Draw the image
    win.blit(image, (x, y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
'''





'''gif image'''

'''import pygame
from PIL import Image

pygame.init()

# Create the window
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Bissom Blast")

# Load the GIF and extract frames
gif = Image.open(r"C:\rithika\pygame install\giphy.gif")
frames = []

# Convert each frame to a format that Pygame can use
for frame in range(gif.n_frames):
    gif.seek(frame)
    frame_image = gif.convert("RGBA")
    frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    frames.append(frame_surface)

# Initialize variables
x = 100
y = 100
width, height = frames[0].get_size()
vel = 10
frame_index = 0
frame_delay = 40 # Delay between frames in milliseconds
last_update_time = pygame.time.get_ticks()

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    
    # Move right
    if keys[pygame.K_RIGHT] and x < 1000 - width:
        x += vel
    
    # Move up
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    
    # Move down
    if keys[pygame.K_DOWN] and y < 700 - height:
        y += vel

    # Update the current frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > frame_delay:
        frame_index = (frame_index + 1) % len(frames)
        last_update_time = current_time

    # Fill the window with black
    win.fill((0, 0, 0))

    # Draw the current frame of the GIF
    win.blit(frames[frame_index], (x, y))

    # Update the display
    pygame.display.update()

# Close the pygame window
pygame.quit()'''



import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Collect Points Example')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - player_size - 10]
player_speed = 5

collectible_size = 30
num_collectibles = 5
collectibles = []
collectible_speed = 5
collectible_points = 10

score = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 35)

# Initialize collectibles
for _ in range(num_collectibles):
    x = random.randint(0, SCREEN_WIDTH - collectible_size)
    y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
    collectibles.append([x, y])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    
    # Ensure the player stays within screen bounds
    player_pos[0] = max(0, min(SCREEN_WIDTH - player_size, player_pos[0]))

    # Update collectibles position
    for collectible in collectibles:
        collectible[1] += collectible_speed
    
    # Collision detection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    
    # Check for collisions with each collectible
    for collectible in collectibles[:]:
        collectible_rect = pygame.Rect(collectible[0], collectible[1], collectible_size, collectible_size)
        if player_rect.colliderect(collectible_rect):
            score += collectible_points
            collectibles.remove(collectible)  # Remove collected collectible
            # Add a new collectible at a random position at the top
            new_collectible = [random.randint(0, SCREEN_WIDTH - collectible_size), 0]
            collectibles.append(new_collectible)
    
    # Reset collectibles that go off screen
    for collectible in collectibles:
        if collectible[1] > SCREEN_HEIGHT:
            collectible[0] = random.randint(0, SCREEN_WIDTH - collectible_size)
            collectible[1] = 0

    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw the player
    pygame.draw.rect(screen, GREEN, player_rect)
    
    # Draw all collectibles
    for collectible in collectibles:
        pygame.draw.rect(screen, RED, (collectible[0], collectible[1], collectible_size, collectible_size))
    
    # Display the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(30)

pygame.quit()

