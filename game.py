import pygame
import math
import random
from pygame import mixer
pygame.init()
end = False
# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("DuckxFox")
icon = pygame.image.load('ducky.png')
pygame.display.set_icon(icon)
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY = 10
def show_score(x,y):
	score = font.render("Score :" + str(score_value),True, (255,255,255))
	screen.blit(score,(x,y))

over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over():
	over = over_font.render("GAME OVER",True,(255,255,255))
	screen.blit(over,(200,250))
# player 
playerimg = pygame.image.load('fox.png')
playerX = 370
playerY = 530
playerX_change=0
playerY_change=0
def player(x,y):
	screen.blit(playerimg,(x,y))
#enemy
enemyimg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 6
for i in range(num_of_enemies):
	enemyimg.append(pygame.image.load('rduck.png'))
	enemyX.append(random.randint(64,736))
	enemyY.append(random.randint(64,400))
	enemyX_change.append(0.2)
	enemyY_change.append(50)
def enemy(x,y,i):
	screen.blit(enemyimg[i],(x,y))
# nets
netimg = pygame.image.load('nets.png')
netX = 370
netY = 616
netX_change = 0
netY_change = 0.2
net_state = "ready"
def fire_net(x,y):
	global net_state
	net_state = "fire"
	screen.blit(netimg,(x+16,y+10))
def isCollision(enemyX,enemyY,netX,netY):
	distance = math.sqrt(math.pow(enemyX-netX,2)+ (math.pow(enemyY-netY,2)))
	if distance<27:
		return True
	return False
# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# screen display and movements
run = True
while run:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change=-0.2
			if event.key == pygame.K_RIGHT:
				playerX_change=0.2
			if event.key == pygame.K_SPACE:
				if net_state == "ready":
					netX = playerX
					fire_net(netX,netY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
	#RBG colours(red,green,blue(0-255))
	playerX += playerX_change
	playerY += playerY_change
	if playerX < 0:
		playerX=0
	elif playerX >=736:
		playerX=736
	for i in range(num_of_enemies):
		#game over scenario
		if isCollision(enemyX[i],enemyY[i],playerX,playerY):
			for j in range(num_of_enemies):
				enemyY[j] =2000
				end = True
			break
		if end:
			game_over()
		enemyX[i] += enemyX_change[i]
		if enemyX[i] < 0:
			enemyX_change[i] = 0.2
			enemyY[i]+=enemyY_change[i]
		elif enemyX[i] >=736:
			enemyX_change[i] = -0.2
			enemyY[i]+=enemyY_change[i]
		#collision
		collision = isCollision(enemyX[i],enemyY[i],netX,netY)
		if collision:
			hits = mixer.Sound('hitsound.wav')
			hits.play()
			netY=560
			net_state = "ready"
			score_value+=1
			enemyX[i] = random.randint(64,736)
			enemyY[i] = random.randint(64,400)
		enemy(enemyX[i],enemyY[i],i)
	# net moment
	if netY<=0:
		netY=480
		net_state = "ready"
	if net_state == "fire":
		fire_net(netX,netY)
		netY-=netY_change
	player(playerX,playerY)
	show_score(textX,textY)
	pygame.display.update()