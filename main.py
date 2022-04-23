import math
import string
import pygame
from random import *

import time

from mpmath import mp


pygame.init()
pygame.font.init()



# seed random number generator
#seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 800 #1440
height = 800 #900

screen = pygame.display.set_mode([width, height])

ui_font = pygame.font.SysFont('Comic Sans MS', 14)

running = True

clock = pygame.time.Clock()

start_time = time.time()
total_time = 0

resolution = 10
cols = 1 + math.floor(width / resolution)
rows = 1 + math.floor(height / resolution)

field = []
dot_raius = 2
################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def init():
    global field
    field = []
    for x in range(cols):
        new_row = []
        for y in range(rows):
            new_row.append(random())
        field.append(new_row)
    

def drawEdges(DISPLAY, r, field_array):
    for x in range(len(field_array)):
        for y in range(len(field_array[0])):
            val = round(field_array[x][y]) * 255
            pygame.draw.circle(DISPLAY, (val, val, val), (x * resolution, y * resolution), r)

def calculateMidPoints(grid_point, res):
    x = res * grid_point[0]
    y = res * grid_point[1]
    a = (x + res / 2, y)
    b = (x + res, y + res / 2)
    c = (x + res / 2, y + res)
    d = (x, y + res / 2)
    return [a, b, c, d]

def stateFromField(grid_point, field_array):
    state = -1
    if grid_point[0] >= 0 and grid_point[0] < (len(field_array) - 1) and grid_point[1] >= 0 and grid_point[1] < (len(field_array[0]) - 1):
        s0 = round(field_array[grid_point[0]][grid_point[1]])
        s1 = round(field_array[grid_point[0] + 1][grid_point[1]])
        s2 = round(field_array[grid_point[0] + 1][grid_point[1] + 1])
        s3 = round(field_array[grid_point[0]][grid_point[1] + 1])
        state = s0 * 8 + s1 * 4 + s2 * 2 + s3 * 1
    return state
################################################################################################
#                                           MAIN LOOP
################################################################################################

init()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##################################################################
    # UPDATE CODE
    ##################################################################

    for i in range(len(field)):
        for j in range(len(field[0])):
            field[i][j] = random()

    ##################################################################
    # DRAW CODE
    ##################################################################

    screen.fill((50, 50, 50))

    drawEdges(screen, dot_raius, field)

    for i in range(len(field) - 1):
        for j in range(len(field[0]) - 1):
            [a, b, c, d] = calculateMidPoints((i, j), resolution)
            state = stateFromField((i, j), field)
            
            if state == 1:
                pygame.draw.line(screen, (255, 255, 255), c, d)
            elif state == 2:
                pygame.draw.line(screen, (255, 255, 255), b, c)
            elif state == 3:
                pygame.draw.line(screen, (255, 255, 255), b, d)
            elif state == 4:
                pygame.draw.line(screen, (255, 255, 255), a, b)
            elif state == 5:
                pygame.draw.line(screen, (255, 255, 255), a, d)
                pygame.draw.line(screen, (255, 255, 255), b, c)
            elif state == 6:
                pygame.draw.line(screen, (255, 255, 255), a, c)
            elif state == 7:
                pygame.draw.line(screen, (255, 255, 255), a, d)
            elif state == 8:
                pygame.draw.line(screen, (255, 255, 255), a, d)
            elif state == 9:
                pygame.draw.line(screen, (255, 255, 255), a, c)
            elif state == 10:
                pygame.draw.line(screen, (255, 255, 255), a, b)
                pygame.draw.line(screen, (255, 255, 255), c, d)
            elif state == 11:
                pygame.draw.line(screen, (255, 255, 255), a, b)
            elif state == 12:
                pygame.draw.line(screen, (255, 255, 255), b, d)
            elif state == 13:
                pygame.draw.line(screen, (255, 255, 255), b, c)
            elif state == 14:
                pygame.draw.line(screen, (255, 255, 255), c, d)
            

    # textsurface = ui_font.render(ui_str, False, (255, 0, 0))
    # screen.blit(textsurface, (0, 0))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(1)
    

# Done! Time to quit.
pygame.quit()