import pygame
from pygame.locals import *
import pygame.sprite
import random

#define variables
seaColor = (12, 15, 95) # navy blue
hitColor = (211, 0, 0) # red
missColor = (230, 230, 230) # white
#define pygame window width
width = 1000
height = 500
sizes = [5, 4, 3, 3, 2] # ship sizes
spacing = 3 # spacing between sea sprite squares
totSpacing = spacing * 11 # total spacing for sea sprite squares
spriteSize = 30 # width and height of sea sprite square
startBufferX = 100 # top right corner buffer
startBufferY = 100 # top right corner buffer
letter_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
number_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Sea Square Sprite Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill(seaColor)
        self.rect = self.image.get_rect()
        self.empty = True
        self.ship = None

# For each size, create a corresponding ship object
def create_ships(sizes):
    ships = []
    for size in sizes:
        ship = Ship(size)
        ships.append(ship)

    return ships

'''Place a valid vertical ship onto the Sea Sprite grid
    where currship is the ship object being placed, shipSize
    is the size of that ship, sprites are the Sea Sprite grid 
    array, and ship_sprites are the sprites that contain a ship'''  
def verticalShip(currship, shipSize, sprites, ship_sprites):
    found = False
    valid = True
    while not found:
        randomNum = random.randint(0, 99)
        if (randomNum + (shipSize * 10) <= 99):
            j = randomNum
            valid = True
            while (j < randomNum + (shipSize * 10)):
                if (sprites.sprites()[j].empty == False):
                    valid = False
                j += 10
            if valid:
                j = randomNum
                while (j < randomNum + (shipSize * 10)):
                    sprites.sprites()[j].empty = False
                    sprites.sprites()[j].ship = currship
                    ship_sprites.add(sprites.sprites()[j])
                    j += 10    
                found = True

'''Place a valid horizontal ship onto the Sea Sprite grid
    where currship is the ship object being placed, shipSize
    is the size of that ship, sprites are the Sea Sprite grid 
    array, and ship_sprites are the sprites that contain a ship'''                                
def horizontalShip(currship, shipSize, sprites, ship_sprites):
    found = False
    valid = True
    while not found:    # while ship position is not found
        randomNum = random.randint(0, 99)
        if ((randomNum + shipSize) % 10 > randomNum % 10) :
            j = randomNum
            valid = True
            while (j < randomNum + shipSize):
                if (sprites.sprites()[j].empty == False):
                    valid = False
                j += 1
            if valid:
                j = randomNum
                while (j < randomNum + shipSize):
                    sprites.sprites()[j].empty = False
                    sprites.sprites()[j].ship = currship
                    ship_sprites.add(sprites.sprites()[j])
                    j += 1    
                found = True      

# Define a ship object with a size and delegated sprites                
class Ship:
    def __init__(self, size):
        self.size = size
        self.ship_sprites = pygame.sprite.Group()

# Define a function that places a ship of each size in the grid of sprites        
def place_ships(ships, sprites):
    for ship in ships:
        randOrientation = random.randint(1, 2)
        if randOrientation == 1:
            verticalShip(ship, ship.size, sprites, ship.ship_sprites)
        else:
            horizontalShip(ship, ship.size, sprites, ship.ship_sprites)

# checks to see if current ship is still afloat            
def check_ship_float_status(ship):
    for sprite in ship.ship_sprites:
        if not sprite.empty:
            return True
    return False

# Displays and runs the game (called in main.py via screen_manager)            
def GameScreen():
    enemy_sprites = pygame.sprite.Group()
    ally_sprites = pygame.sprite.Group()
    
    enemy_sprite_positions = [
        ((spriteSize + spacing) * col + spacing + startBufferX, (spriteSize + spacing) * row + spacing + startBufferY)
        for row in range(10)
        for col in range(10)
    ]

    ally_sprite_positions = [
        ((spriteSize + spacing) * col + spacing + startBufferX + height, (spriteSize + spacing) * row + spacing + startBufferY)
        for row in range(10)
        for col in range(10)
    ]
    
    for position in enemy_sprite_positions:
        sprite = Sprite(spriteSize, spriteSize)
        sprite.image = pygame.Surface((spriteSize, spriteSize))
        sprite.image.fill(seaColor) 
        sprite.rect = sprite.image.get_rect()
        sprite.rect.topleft = position
        enemy_sprites.add(sprite)
    
    for position in ally_sprite_positions:
        sprite = Sprite(spriteSize, spriteSize)
        sprite.image = pygame.Surface((spriteSize, spriteSize))
        sprite.image.fill(seaColor) 
        sprite.rect = sprite.image.get_rect()
        sprite.rect.topleft = position
        ally_sprites.add(sprite)
    
    ships = create_ships(sizes)
    place_ships(ships, enemy_sprites)
    turnCounter = 0
    shipCounter = len(sizes)
    running = True
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [sprite for sprite in enemy_sprites if sprite.rect.collidepoint(pos)]
                for sprite in clicked_sprites:
                    sprite_width, sprite_height = sprite.image.get_size()
                    local_pos = pos[0] - sprite.rect.left, pos[1] - sprite.rect.top
                    if (0 <= local_pos[0] < sprite_width) and (0 <= local_pos[1] < sprite_height):
                        if (sprite.image.get_at(local_pos) == seaColor and not sprite.empty) :
                            sprite.image.fill(hitColor)
                            sprite.empty = True
                            if not check_ship_float_status(sprite.ship):
                                shipCounter -= 1
                            turnCounter += 1
                        elif (sprite.image.get_at(local_pos) == seaColor):
                            sprite.image.fill(missColor)
                            turnCounter += 1

        enemy_sprites.update()
        ally_sprites.update()
        
        screen.fill((0, 0, 0))
        
        # Draw letter labels for enemy grid
        for i, label in enumerate(letter_labels):
            font = pygame.font.Font(None, 24)
            text = font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=((spriteSize + spacing) * i + startBufferX + spriteSize // 2, startBufferY - 20))
            screen.blit(text, text_rect)

        # Draw number labels for enemy grid
        for i, label in enumerate(number_labels):
            font = pygame.font.Font(None, 24)
            text = font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=(startBufferX - 20, (spriteSize + spacing) * i + startBufferY + spriteSize // 2))
            screen.blit(text, text_rect)

        # Draw letter labels for ally grid
        for i, label in enumerate(letter_labels):
            font = pygame.font.Font(None, 24)
            text = font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=((spriteSize + spacing) * i + startBufferX + height + spriteSize // 2, startBufferY - 20))
            screen.blit(text, text_rect)

        # Draw number labels for ally grid
        for i, label in enumerate(number_labels):
            font = pygame.font.Font(None, 24)
            text = font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=(startBufferX + height - 20, (spriteSize + spacing) * i + startBufferY + spriteSize // 2))
            screen.blit(text, text_rect)
            
        enemy_sprites.draw(screen)
        ally_sprites.draw(screen)

        font = pygame.font.Font(None, 36)
        turn_count_text = font.render("Turns: " + str(turnCounter), True, (255, 255, 255))
        turn_count_text_rect = turn_count_text.get_rect()
        turn_count_text_rect.center = (width // 2 - 70, 20)
        screen.blit(turn_count_text, turn_count_text_rect)
        
        ship_count_text = font.render("Ships Left: " + str(shipCounter), True, (255, 255, 255))
        ship_count_text_rect = turn_count_text.get_rect()
        ship_count_text_rect.center = (width // 2 + 70, 20)
        screen.blit(ship_count_text, ship_count_text_rect)

        pygame.display.flip()
        clock.tick(60)