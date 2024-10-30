import pygame
from time import sleep
from decimal import Decimal, getcontext
pygame.init()
infoObject = pygame.display.Info()
width = infoObject.current_w // 10
height = infoObject.current_h // 10
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
font = pygame.font.Font(None, 10)

getcontext().prec = width * height

positions = [0, 15, 30]

n=1
def factorial(num):
    if(isinstance(num, int) and (num >= 0)):
        if (num == 0):
            return 1
        else:
            return num * factorial(num - 1)
    else:
        raise ValueError("Error: Missing parameters.")
while True:
    realEuler=Decimal(0)
    for i in range(0, n):
        realEuler += Decimal(1) / factorial(i)
    segmentedEuler = []
    for i in range(0, height):
        segmentedEuler.append()
    for i in range(0, height):
        eulerText = font.render(str(segmentedEuler[i]), 1, "white")
        screen.blit(eulerText)
    sleep(0.1)
    n+=1