import pygame

pygame.init()

# Text
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

# Screen
WIDTH = 1000
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 60
gravity = -0.75

# Player Settings
playerx = 500
playery = 225
player_ground = True
down_vel = 0

def player_movement(playerx, playery, player_ground, down_vel):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and w:
        playerx -= 10

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerx += 10

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_ground:
        down_vel = 17
        player_ground = False

    if not player_ground:
        playery -= down_vel
        if down_vel > -10:
            down_vel += gravity
    else:
        down_vel = 0

    if playery < 400:
        player_ground = False
    else:
        player_ground = True

    return playerx, playery, player_ground, down_vel

while running:

    playerx, playery, player_ground, down_vel = player_movement(playerx, playery, player_ground, down_vel)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), [playerx, playery, 48, 64])
    pygame.display.update()
    clock.tick(FPS)


