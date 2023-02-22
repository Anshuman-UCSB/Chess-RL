import pygame
from utils import *
from time import sleep
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from board import Board

pygame.init()

sq_size = 80

SCREEN_WIDTH = sq_size*8
SCREEN_HEIGHT = sq_size*8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess - Reinforcement Learning")

running = True
white = (240,217,181)
black = (181,136,99)
b = Board()

imgs = {}
for l in "pnbrqk":
	imgs[l] = pygame.image.load("imgs/white/"+l+".png")
	imgs[l.upper()] = pygame.image.load("imgs/black/"+l+".png")
isWhite = True
while running:
	for y in range(0,SCREEN_HEIGHT,sq_size):
		for x in range(0,SCREEN_HEIGHT,sq_size):
			screen.fill(white if isWhite else black,(x,y,sq_size,sq_size))
			isWhite = not isWhite
		isWhite = not isWhite
	for y in range(0,8):
		for x in range(0,8):
			p=b.at(Point(x,y))
			if p:
				screen.blit(imgs[str(p)[0]],(x*sq_size+sq_size*.1,SCREEN_HEIGHT-sq_size-(y*sq_size-sq_size*.1)))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			running = False
		if event.type == MOUSEBUTTONUP:
			x,y=event.pos
			x//=sq_size
			y//=sq_size
			pos = XYtoLN(x, y)
			if b.whiteTurn and b.at(pos) and b.at(pos).white:
				print(b.at(pos).moves(b))
pygame.quit()