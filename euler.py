import pygame
from time import sleep
from decimal import Decimal, getcontext
pygame.init()
infoObject = pygame.display.Info()
sizeSelected = input("Size(1, 2, 3): ")
if not sizeSelected in ["1", "2", "3"]:
    raise ValueError("Incorrect size selected")
slowDown = float(input("Enter the slowdown in seconds(0.1 recommended): "))
if slowDown < 0:
    raise ValueError("Slowdown below 0")
changeColor = input("Want to change default white color(S/n)? ").lower()
if changeColor == "s":
    color1 = int(input("Enter the red color(0, 255): "))
    color2 = int(input("Enter the green color(0, 255): "))
    color3 = int(input("Enter the blue color(0, 255): "))
    color = color1, color2, color3
else:
    color = 255, 255, 255#White
if(sizeSelected == "1"):
    font = pygame.font.Font(None, 15)
    surface = font.render("0", True, color)
    sizeHeight = surface.get_height()
    sizeWidth = surface.get_width()
elif(sizeSelected == "2"):
    font = pygame.font.Font(None, 25)
    surface = font.render("0", True, color)
    sizeHeight = surface.get_height()
    sizeWidth = surface.get_width()
elif(sizeSelected == "3"):
    font = pygame.font.Font(None, 40)
    surface = font.render("0", True, color)
    sizeHeight = surface.get_height()
    sizeWidth = surface.get_width()
width = (infoObject.current_w // sizeWidth) - 5 #One less for some margin
height = infoObject.current_h // sizeHeight
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
getcontext().prec = (width * height) - 2
positions = [sizeHeight * i for i in range(height)]
def factorial(num: int) -> int:
    if not (isinstance(num, int) and (num >= 0)):
        raise ValueError("Error: Missing parameters.")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
n=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    realEuler=Decimal(0)
    screen.fill((0, 0, 0))
    for i in range(0, n):
        realEuler += Decimal(1) / Decimal(factorial(i))
    segmentedEuler = []
    realEuler = list(str(realEuler))
    for i in range(0, height):
        actualDecimal = ""
        for i in range(0, width):
            if i < len(realEuler):
                actualDecimal += realEuler.pop(0)
            else:
                actualDecimal += '0'
        segmentedEuler.append(actualDecimal)
    for i in range(0, height):
        eulerText = font.render(str(segmentedEuler[i]), 1, color)
        screen.blit(eulerText, (0, positions[i]))
    pygame.display.flip()
    sleep(slowDown)
    n+=1