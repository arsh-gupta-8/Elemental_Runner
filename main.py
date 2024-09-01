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

# Images
Grassland_BG = pygame.image.load('Background/Grassland.png')

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 60
gravity = -0.75

# Player Settings
playerx = 500
playery = 225
facingRight = True
player_ground = True
down_vel = 0
bullets = []

class Bullet:
    def __init__(self, bulletx, bullety, facingRight):
        self.bulletx = bulletx
        self.bullety = bullety
        self.facingRight = facingRight
        self.speed = 20

    def update_bullet_position(self):
        if self.facingRight:
            self.bulletx += 20
        else:
            self.bulletx -= 20

def player_movement(playerx, playery, player_ground, down_vel, facingRight):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and playerx > 0:
        playerx -= 10
        facingRight = False

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and playerx < WIDTH - 58:
        playerx += 10
        facingRight = True

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_ground:
        down_vel = 17
        player_ground = False

    if not player_ground:
        playery -= down_vel
        if down_vel > -10:
            down_vel += gravity
    else:
        down_vel = 0

    if playery < 385:
        player_ground = False
    else:
        player_ground = True

    return playerx, playery, player_ground, down_vel, facingRight

while running:

    screen.blit(Grassland_BG, (0, 0))

    playerx, playery, player_ground, down_vel, facingRight = player_movement(playerx, playery, player_ground, down_vel, facingRight)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet(playerx, playery, facingRight))

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    for bullet in bullets:
        bullet.update_bullet_position()
        pygame.draw.rect(screen, (0, 0, 0), [bullet.bulletx, bullet.bullety, 25, 10])
        if bullet.bulletx < -25 or bullet.bulletx > WIDTH:
            bullets.remove(bullet)

    # screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), [playerx, playery, 48, 64])
    pygame.display.update()
    clock.tick(FPS)


