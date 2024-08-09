import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("DuckxFox")
icon = pygame.image.load('ducky.png')
pygame.display.set_icon(icon)
playerimg = pygame.image.load('fox.png')
playerX = 370
playerY = 530
playerX_change=0
playerY_change=0
enemyimg = pygame.image.load('rduck.png')
enemyX = random.randint(64,736)
enemyY = random.randint(64,536)
enemyX_change = 0.3
enemyY_change = 50
def enemy(x,y):
	screen.blit(enemyimg,(x,y))
def player(x,y):
	screen.blit(playerimg,(x,y))
run = True
while run:
	screen.fill((0,150,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("left arrow is pressed")
				playerX_change=-0.2
			if event.key == pygame.K_RIGHT:
				print("right key is pressed")
				playerX_change=0.2
			if event.key == pygame.K_UP:
				print("left arrow is pressed")
				playerY_change=-0.2
			if event.key == pygame.K_DOWN:
				print("right key is pressed")
				playerY_change=0.2
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerY_change = 0
				print("key is released")
	#RBG colours(red,green,blue(0-255))
	playerX += playerX_change
	playerY += playerY_change
	if playerX < 0:
		playerX=0
	elif playerX >=736:
		playerX=736
	elif playerY<0:
		playerY=0
	elif playerY>536:
		playerY=536
	enemyX += enemyX_change
	if enemyX < 0:
		enemyX_change = 0.3
		enemyY+=enemyY_change
	elif enemyX >=736:
		enemyX_change = -0.3
		enemyY+=enemyY_change
	player(playerX,playerY)
	enemy(enemyX,enemyY)
	pygame.display.update()