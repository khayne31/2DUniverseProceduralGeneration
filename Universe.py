from pygame.locals import *
import pygame
import random
from math import floor
import time
import sys

pygame.font.init()
WIN_WIDTH = 500
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0,0,0)
NUM_SECTORS = 18
BLUE=(0,0,255)
COORD_FONT = pygame.font.SysFont("comicsans", 25)
sector_width = int(WIN_WIDTH / NUM_SECTORS)
sector_height = int(WIN_HEIGHT / NUM_SECTORS)
color_arr = [(255, 0, 0), (28, 55, 123), (0, 0, 255), (255, 124, 0), (124, 0, 70), (23, 64, 83)]

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
win.fill(BLACK)

pygame.draw.rect(win,BLUE,(200,150,1,1))
offset = [0,0]

global nLehmer

def lehmer(nLehmer = 0):
	nLehmer += 0xe120fc15
	temp = nLehmer * 0x4a39b70d
	m1 = (temp >> 32) ^ temp
	temp = m1 * 0x12fad5c9
	m2 = (temp >> 32) ^ temp
	return m2	

def randomInt(min, max, seed):
	return lehmer(seed) % (max - min) + min


def star_exists(x, y, win_x, win_y):
	seed = (x & 0xFFFF) << 16 | (y & 0xFFFF)

	star_exists = randomInt(0, 15, seed) == 1

	if not star_exists:
		return None


	pygame.draw.circle(win, color_arr[randomInt(1, len(color_arr) - 1, seed)], (win_x + int(sector_width / 2), win_y +   int(sector_height / 2)), randomInt(int(sector_width * .1), floor(sector_width / 2), seed))

	

def draw_static():
	random.seed(1000)

	keys=pygame.key.get_pressed()
	if keys[K_RIGHT]:
		offset[0] += 1
	if keys[K_LEFT]:
		offset[0] -= 1
	if keys[K_UP]:
		offset[1] -= 1
	if keys[K_DOWN]:
		offset[1] += 1

	mouse_x = 0 
	mouse_y = 0
	for i in range(NUM_SECTORS):
		for j in range(NUM_SECTORS):

			mouse_x = i * sector_width
			mouse_y = j * sector_height

			y = (i+offset[0]) * sector_width
			x = (j+offset[1]) * sector_height

			
			star_exists(x,y, mouse_x, mouse_y)
			if i == 0 and j == 0:
				cord_text = COORD_FONT.render("({}, {})".format(y, x), 1, (255, 255, 255))
				win.blit(cord_text, (10, 10))
		





while True:
	win.fill(BLACK)
	for event in pygame.event.get():
	    if event.type==QUIT:
	        pygame.quit()
	        sys.exit()
	draw_static()
	pygame.display.update()
	time.sleep(.01)

