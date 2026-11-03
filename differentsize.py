'''import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blossom Blast")

# Load and scale the image
image_path = r"C:\rithika\pygame install\stars.png"
image = pygame.image.load(image_path)
width = int(image.get_width() * 0.1)
height = int(image.get_height() * 0.1)
image = pygame.transform.scale(image, (width, height))

# Player properties
player_x = 600
player_y = 600
player_vel = 10

# Collectible properties
collectible_sizes = [20, 30, 40]  # Sizes of the collectibles
collectible_points = {20: 2, 30: 3, 40: 5}  # Points for each size
num_collectibles = 5
collectibles = []
collectible_speed = 5

# Initialize collectibles
for _ in range(num_collectibles):
    size = random.choice(collectible_sizes)
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
    collectibles.append([x, y, size])

# Game variables
score = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 35)

# Game loop
running = True
while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - width:
        player_x += player_vel

    # Update collectible positions
    for collectible in collectibles:
        collectible[1] += collectible_speed

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, width, height)
    
    for collectible in collectibles[:]:
        collectible_rect = pygame.Rect(collectible[0], collectible[1], collectible[2], collectible[2])
        if player_rect.colliderect(collectible_rect):
            score += collectible_points[collectible[2]]
            collectibles.remove(collectible)  # Remove collected collectible
            # Add a new collectible at a random position at the top
            new_size = random.choice(collectible_sizes)
            new_collectible = [random.randint(0, SCREEN_WIDTH - new_size), 0, new_size]
            collectibles.append(new_collectible)
    
    # Reset collectibles that go off screen
    for collectible in collectibles:
        if collectible[1] > SCREEN_HEIGHT:
            size = random.choice(collectible_sizes)
            collectible[0] = random.randint(0, SCREEN_WIDTH - size)
            collectible[1] = 0
            collectible[2] = size

    # Fill the screen with black
    win.fill((0, 0, 0))

    # Draw the player image
    win.blit(image, (player_x, player_y))
    
    # Draw all collectibles
    for collectible in collectibles:
        pygame.draw.rect(win, (255, 0, 0), (collectible[0], collectible[1], collectible[2], collectible[2]))
    
    # Display the score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()'''



import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blossom Blast")

# Load and scale the image
image_path = r"C:\rithika\pygame install\stars.png"
image = pygame.image.load(image_path)
width = int(image.get_width() * 0.1)
height = int(image.get_height() * 0.1)
image = pygame.transform.scale(image, (width, height))

# Player properties
player_x = 600
player_y = 600
player_vel = 10

# Collectible properties
collectible_sizes = [20, 30, 40]  # Sizes of the collectibles
collectible_points = {20: 2, 30: 3, 40: 5}  # Points for each size
circle_size = 30
circle_speed_boost = 10  # Speed increase
boost_duration = 20  # Duration of the speed boost in seconds

num_collectibles = 5
collectibles = []
collectible_speed = 5
speed_boost_active = False
boost_start_time = 0

# Initialize collectibles
for _ in range(num_collectibles):
    size = random.choice(collectible_sizes)
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
    collectibles.append([x, y, size, 'square'])

# Add initial circle object
circle_x = random.randint(0, SCREEN_WIDTH - circle_size)
circle_y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
collectibles.append([circle_x, circle_y, circle_size, 'circle'])

# Game variables
score = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 35)

# Game loop
running = True
while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - width:
        player_x += player_vel

    # Update collectible positions
    for collectible in collectibles:
        collectible[1] += collectible_speed if not speed_boost_active else collectible_speed + circle_speed_boost

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, width, height)
    
    for collectible in collectibles[:]:
        collectible_rect = pygame.Rect(collectible[0], collectible[1], collectible[2], collectible[2])
        if player_rect.colliderect(collectible_rect):
            if collectible[3] == 'square':
                # Handle square collectible
                score += collectible_points[collectible[2]]
                collectibles.remove(collectible)  # Remove collected collectible
                # Add a new square collectible at a random position at the top
                new_size = random.choice(collectible_sizes)
                new_collectible = [random.randint(0, SCREEN_WIDTH - new_size), 0, new_size, 'square']
                collectibles.append(new_collectible)
            elif collectible[3] == 'circle':
                # Handle circle collectible
                collectibles.remove(collectible)  # Remove collected circle
                # Add a new circle collectible at a random position at the top
                circle_x = random.randint(0, SCREEN_WIDTH - circle_size)
                circle_y = random.randint(-SCREEN_HEIGHT, 0)
                collectibles.append([circle_x, circle_y, circle_size, 'circle'])
                # Activate speed boost
                speed_boost_active = True
                boost_start_time = time.time()
    
    # Reset collectibles that go off screen
    for collectible in collectibles:
        if collectible[1] > SCREEN_HEIGHT:
            if collectible[3] == 'square':
                size = random.choice(collectible_sizes)
                collectible[0] = random.randint(0, SCREEN_WIDTH - size)
                collectible[1] = 0
                collectible[2] = size
            elif collectible[3] == 'circle':
                collectible[0] = random.randint(0, SCREEN_WIDTH - circle_size)
                collectible[1] = 0

    # Check if boost duration has ended
    if speed_boost_active and (time.time() - boost_start_time) > boost_duration:
        speed_boost_active = False

    # Fill the screen with black
    win.fill((0, 0, 0))

    # Draw the player image
    win.blit(image, (player_x, player_y))
    
    # Draw all collectibles
    for collectible in collectibles:
        if collectible[3] == 'square':
            pygame.draw.rect(win, (255, 0, 0), (collectible[0], collectible[1], collectible[2], collectible[2]))
        elif collectible[3] == 'circle':
            pygame.draw.circle(win, (0, 255, 0), (collectible[0] + circle_size // 2, collectible[1] + circle_size // 2), circle_size // 2)
    
    # Display the score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blossom Blast")

# Load and scale the image
image_path = r"C:\rithika\pygame install\stars.png"
image = pygame.image.load(image_path)
width = int(image.get_width() * 0.1)
height = int(image.get_height() * 0.1)
image = pygame.transform.scale(image, (width, height))

# Player properties
player_x = 600
player_y = 600
player_vel = 10

# Collectible properties
collectible_sizes = [20, 30, 40]  # Sizes of the collectibles
collectible_points = {20: 2, 30: 3, 40: 5}  # Points for each size
circle_size = 30
circle_speed_boost = 10  # Speed increase
boost_duration = 20  # Duration of the speed boost in seconds

num_collectibles = 5
collectibles = []
collectible_speed = 5
speed_boost_active = False
boost_start_time = 0

# Initialize collectibles
for _ in range(num_collectibles):
    size = random.choice(collectible_sizes)
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
    collectibles.append([x, y, size, 'square'])

# Add initial circle object
circle_x = random.randint(0, SCREEN_WIDTH - circle_size)
circle_y = random.randint(-SCREEN_HEIGHT, 0)  # Start above the screen
collectibles.append([circle_x, circle_y, circle_size, 'circle'])

# Game variables
score = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 35)

# Game loop
running = True
while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - width:
        player_x += player_vel

    # Update collectible positions
    for collectible in collectibles:
        collectible[1] += collectible_speed if not speed_boost_active else collectible_speed + circle_speed_boost

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, width, height)
    
    for collectible in collectibles[:]:
        collectible_rect = pygame.Rect(collectible[0], collectible[1], collectible[2], collectible[2])
        if player_rect.colliderect(collectible_rect):
            if collectible[3] == 'square':
                # Handle square collectible
                score += collectible_points[collectible[2]]
                collectibles.remove(collectible)  # Remove collected collectible
                # Add a new square collectible at a random position at the top
                new_size = random.choice(collectible_sizes)
                new_collectible = [random.randint(0, SCREEN_WIDTH - new_size), 0, new_size, 'square']
                collectibles.append(new_collectible)
            elif collectible[3] == 'circle':
                # Handle circle collectible
                collectibles.remove(collectible)  # Remove collected circle
                # Add a new circle collectible at a random position at the top
                circle_x = random.randint(0, SCREEN_WIDTH - circle_size)
                circle_y = random.randint(-SCREEN_HEIGHT, 0)
                collectibles.append([circle_x, circle_y, circle_size, 'circle'])
                # Activate speed boost
                speed_boost_active = True
                boost_start_time = time.time()
    
    # Reset collectibles that go off screen
    for collectible in collectibles:
        if collectible[1] > SCREEN_HEIGHT:
            if collectible[3] == 'square':
                size = random.choice(collectible_sizes)
                collectible[0] = random.randint(0, SCREEN_WIDTH - size)
                collectible[1] = 0
                collectible[2] = size
            elif collectible[3] == 'circle':
                collectible[0] = random.randint(0, SCREEN_WIDTH - circle_size)
                collectible[1] = 0

    # Check if boost duration has ended
    if speed_boost_active and (time.time() - boost_start_time) > boost_duration:
        speed_boost_active = False

    # Fill the screen with black
    win.fill((0, 0, 0))

    # Draw the player image
    win.blit(image, (player_x, player_y))
    
    # Draw all collectibles
    for collectible in collectibles:
        if collectible[3] == 'square':
            pygame.draw.rect(win, (255, 0, 0), (collectible[0], collectible[1], collectible[2], collectible[2]))
        elif collectible[3] == 'circle':
            pygame.draw.circle(win, (0, 255, 0), (collectible[0] + circle_size // 2, collectible[1] + circle_size // 2), circle_size // 2)
    
    # Display the score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
