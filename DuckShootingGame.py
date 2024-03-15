import sys
import pygame
import random

## Game Setup

pygame.init()

pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((1280,720)) #(Width, Height) of screen
clock = pygame.time.Clock() # Determines frame rate

wood_bg = pygame.image.load('wood_image.jpg')
land_bg = pygame.image.load('grass_image.png')
water_bg = pygame.image.load('water_image.png')

crosshair = pygame.image.load('crosshair.png')
crosshair = pygame.transform.scale(crosshair, (200,200))

target = pygame.image.load('target_image.png')
target = pygame.transform.scale(target, (200,200))

landY = 250
landSpeed = 1

waterY = 550
waterSpeed = 2

targetList = []
for _ in range(20):
    targetX = random.randrange(50, 1230)
    targetY = random.randrange(200, 620)
    targetHitBox = target.get_rect(center = (targetX, targetY))
    targetList.append(targetHitBox)

## Run Game
while True: #Creates the play loop to run endlessly until the loop breaks
    for event in pygame.event.get(): # Looks for events in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos) # Puts a rectangle around the center of the mouse. event.pos is the mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, t in enumerate(targetList):
                if crosshair_rect.colliderect(t):
                    del targetList[i]
            
    screen.blit(wood_bg,(0,0)) # (Item you want to display, (X,Y)) (0,0) is top Left
    
    landY -= landSpeed
    if landY <= 200 or landY >= 300:
        landSpeed *= -1
    screen.blit(land_bg,(0,landY)) 

    for t in targetList:
        screen.blit(target, t)

    screen.blit(crosshair, (crosshair_rect.x-90,crosshair_rect.y+45))

    waterY -= waterSpeed
    if waterY <= 500 or waterY >= 650:
        waterSpeed *= -1
    screen.blit(water_bg,(0,waterY)) 

    pygame.display.update()
    clock.tick(120)