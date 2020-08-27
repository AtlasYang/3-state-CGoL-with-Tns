# 2020/08/27
# Conway's Game of Life Expansion Project by Atlas Yang

import numpy as np
import sys, random
import pygame
from pygame.locals import *

pygame.init()

# User input
WIDTH = int(input('Input width(720~1080p recommended): '))
HEIGHT = int(input('Input height(480~720p recommended): '))
LEN = int(input('Input cell size(5~20p recommended): '))
print('Click to change state of each cell.')
print('Press n to process 1 step with alternative rules.')
print('Press m to process 1 step with original rules. Have fun!')

# display surface set
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
pygame.display.set_icon(pygame.image.load('gameicon.png'))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)                              
BLUE = (0, 0, 255)
YELLOW = (128, 128, 0)
ORANGE = (160, 100, 0)
SKYBLUE = (0, 128, 128)

state1_color = WHITE
state2_color = GREY
edge_color = GREY


cellMap = []
posMap = []
for i in range(int((WIDTH/LEN)*(HEIGHT/LEN))):
    cellMap.append(0)

#random generating code
#cellMap = [random.randint(0, 2) for i in range(int((WIDTH/LEN)*(HEIGHT/LEN)))]

for j in range(0, HEIGHT, LEN):
    for i in range(0, WIDTH, LEN):
        posMap.append([i, j])

def s01(n):
    if n == 0:
        return 0
    else:
        return 1

def sum_neighbor(i):
    return (s01(cellMap[i-int(WIDTH/LEN) + 1]) + s01(cellMap[i-int(WIDTH/LEN)]) 
    + s01(cellMap[i-int(WIDTH/LEN)-1]) + s01(cellMap[i-1]) + s01(cellMap[i+1])
    + s01(cellMap[i+int(WIDTH/LEN)+1]) + s01(cellMap[i+int(WIDTH/LEN)])
    + s01(cellMap[i+int(WIDTH/LEN)-1]))
            

# Visualizing Functions
def draw_sq(pos, state):
    recta = (pos[0], pos[1], LEN, LEN)
    if state == 1:
        pygame.draw.rect(DISPLAYSURF, state1_color, recta)
        return
    elif state == 2:
        pygame.draw.rect(DISPLAYSURF, state2_color, recta)
        return
    elif state == 0:
        return

def draw_edgeline():
    for i in range(0, WIDTH+LEN, LEN):
        pygame.draw.line(DISPLAYSURF, edge_color, (i, 0), (i, HEIGHT))
    for j in range(0, HEIGHT+LEN, LEN):
        pygame.draw.line(DISPLAYSURF, edge_color, (0, j), (WIDTH, j))

def graphize():
    for i in range(len(cellMap)):
        draw_sq(posMap[i], cellMap[i])


# State transition matrix(Examples)

# A. Blinker: Most of the pattern is periodic and blinks
#T = np.array([[0, 0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 1, 1, 2, 2, 0, 0, 0], [0, 0, 2, 2, 1, 1, 0, 0, 0]])

# B. Growing Tiles: Most patterns grow slowly but infinitely. Starting with 3 by 3 "+" creates cool patterns
#T = np.array([[0, 0, 0, 1, 2, 0, 0, 0, 0], [0, 0, 1, 2, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 0]])

# C. Explosive: Small inition pattern explode vert fast and self-
# T = np.array([[0, 1, 0, 2, 0, 1, 0, 2, 0], [0, 0, 1, 2, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 0]])

# D. Oriental Patterns: Try starting with 1-D shape like dot or line. Oriental, Aesthetic patterns appear.
T = np.array([[0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0, 0, 0], [0, 2, 0, 1, 0, 0, 0, 0, 0]])


# Original GoL rule.
t = []
def process():
    global cellMap, t
    for i in range(len(cellMap)):
        try:
            s = sum_neighbor(i)
            if s<=1 or s>=4:
                t.append(0)
            elif s == 3:
                t.append(1)
            else:
                t.append(cellMap[i])
        except:
            t.append(cellMap[i])
    cellMap = t
    t = []
    return

# Alternative rule. Uses TNS method.
def process_alternative():
    global cellMap, t, T
    for i in range(len(cellMap)):
        try:
            n_sum = sum_neighbor(i)
            n = np.zeros(9)
            n[n_sum] = 1
            s = np.zeros(T.shape[0])
            s[cellMap[i]] = 1
            res = np.dot(np.dot(T, n), s)
            t.append(int(res))
        except:
            t.append(cellMap[i])
    cellMap = t
    t = []
    return


pos = [-1, -1]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = list(event.pos)
            for i in range(len(posMap)):
                if pos[0]  < posMap[i][0]:
                    pos[0] = posMap[i-1][0]
                    break
            for i in range(len(posMap)):
                if pos[1] < posMap[i][1]:
                    pos[1] = posMap[i-int((WIDTH/LEN))][1]
                    break
        elif event.type == KEYDOWN:
            if event.key == K_n:
                process_alternative()
                DISPLAYSURF.fill(BLACK)
                draw_edgeline()
                graphize()
                draw_edgeline()
                pygame.display.update()
            if event.key == K_m:
                process() 
                DISPLAYSURF.fill(BLACK)
                graphize()
                draw_edgeline()
                pygame.display.update()

    index = -1
    for j in range(len(posMap)):
	    if posMap[j] == pos:
    		index = j


    if not index == -1:
        if cellMap[index] == 0:
            cellMap[index] = 1
        elif cellMap[index] == 1:
            cellMap[index] = 2
        elif cellMap[index] == 2:
            cellMap[index] = 0
        pos = [-1, -1]
        index = -1
  
    DISPLAYSURF.fill(BLACK)
    graphize()
    draw_edgeline()
    pygame.display.update()
    
        
            
