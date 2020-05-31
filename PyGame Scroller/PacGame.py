#Creating a game 
#Import game library
import pygame 
#Import to generate random numbers.
import random 

# Import pygame.locals for easier access to key coordinates to move player and quit.
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Define the Player object extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Define the enemy object extending pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


#Define the prize object extending pygame.sprite.Sprite
class Prize(pygame.sprite.Sprite):
    def __init__(self):
        super(Prize, self).__init__()
        self.surf = pygame.image.load("prize.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    # Move the prize based on a constant speed
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

#Initialize the pygame modules to get everything started.
pygame.init() 
pygame.display.set_caption("Game On")
#The screen that will be created needs a width and a height.
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

#Create custom events for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDPRIZE = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPRIZE, 1000)

#Creating the player and prize
player = Player()

enemies = pygame.sprite.Group()
prize = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


#Initialize variable to run the game loop 
running = True
#This is the game loop.
while running:
    #Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            #if the user clicks the Escape key, stop the loop
            if event.key == K_ESCAPE:
                running = False

        #if the user clicks the window close button, stop the loop
        elif event.type == QUIT:
            running = False

        #adding a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

         # Should we add a new cloud?
        elif event.type == ADDPRIZE:
            # Create the new cloud, and add it to our sprite groups
            new_prize = Prize()
            prize.add(new_prize)
            all_sprites.add(new_prize)

# Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies
    enemies.update()
    prize.update()

# Fill the screen with black
    screen.fill((0, 0, 0))

# Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player
        player.kill()
        print("You lose!")

        # Stop the loop
        running = False

    if pygame.sprite.spritecollideany(player, prize):
        # If so, remove the player
        player.kill()
        print("You win!")

        # Stop the loop
        running = False

    #update screen
    pygame.display.flip()
    clock.tick(30)
