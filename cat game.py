import pygame
import math
import random
import sys
import os
import time

pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
myGray = (75,75,75)
BLUE = (0,0,200)
GRAY = (110,110,110)
RED = (255,0,0)
YELLOW = (255,255,0)
lightBlue = (0,170,170)
lightYellow = (239,179,105)
LIGHTGREEN = (104, 244, 66)
DARKGREEN = (29, 119, 4)


myFont = pygame.font.SysFont("Segoe UI Black", 36)
myFontSmall = pygame.font.SysFont("Segoe UI Black", 24)
myFontSmaller = pygame.font.SysFont("Segoe UI Black", 14)
myFontLarge = pygame.font.SysFont("Segoe UI Black", 48)


selectIcon = pygame.image.load("mugiwara_select.png")
selectIcon = pygame.transform.scale(selectIcon, (45,45))

x_markIcon = pygame.image.load("x_mark2.png")
x_markIcon = pygame.transform.scale(x_markIcon, (200,200))

o_markIcon = pygame.image.load("circle_mark.png")
o_markIcon = pygame.transform.scale(o_markIcon, (200,200))

#E: x, y, width, height, surface, color, icon, moveRight, moveDown
#S: True
#Retorna True si se apreta en el area delimitada. (Es un boton)

def singleButton(x,y, width, height, surface, color, icon, moveRight, moveDown):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    radius = 18

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.circle(surface, color, (x + moveRight, y + moveDown), radius)
        surface.blit(icon, (x, y))
        
        if click[0] == 1:
            return True    

#E: x,y, width, height, surface, color
#S: True
#D: Retorna True si se apreta en el area delimitada. Este boton solo funciona para el menu
    
def buttonInGame(x,y, width, height, surface, moveRight, moveDown):

    global selectIcon
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        surface.blit(selectIcon, (x - 45, y - moveDown))
        surface.blit(selectIcon, (x + moveRight, y - moveDown))

        if click[0] == 1:
            return True
    pygame.display.update()


#E: x,y, width, height, surface, color
#S: True
#D: Retorna True si se apreta en el area delimitada. Este boton solo funciona para el menu  (este boton no muestra ninguna imagen)

def buttonInGameVer2(x,y, width, height, surface):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            return True
    pygame.display.update()


#E: eje x, y, width, height, surface
#S: True
#D: Retorna True si el mouse se encuentra dentro del area delimitada

def inArea(x,y, width, height, surface):

    mouse = pygame.mouse.get_pos()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        return True
    
def shortestPathValueCat(matrix, rowPos, colPos):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    pathValue = 10000000
    
    #check right path
    path = 0
    for col in range(colPos + 1, numColumns):
        path += matrix[rowPos][col]
    if path <= pathValue:
        pathValue = path

    #check left path
    path = 0
    for col in range(colPos):
        path += matrix[rowPos][col]
    if path <= pathValue:
        pathValue = path

    #check upper path
    path = 0
    for row in range(rowPos):
        path += matrix[row][colPos]
    if path <= pathValue:
        pathValue = path

    #check under path
    path = 0
    for row in range(rowPos + 1, numRows):
        path += matrix[row][colPos]
    if path <= pathValue:
        pathValue = path

##    if rowPos % 2 != 0:
##        #check right positive diagonal
##        path = 0
##        for pos in range(1, rowPos + 1):
##            path += matrix[pos - 1][-pos]
##        if path <= pathValue:
##            pathValue = path
##            
##        #check right negative diagonal
##        path = 0
##        for pos in range(rowPos + 1, numRows):
##            path += matrix[pos][pos]
##        if path <= pathValue:
##            pathValue = path
##
##    if rowPos % 2 == 0:
##        #check left positive diagonal
##        path = 0
##        for pos in range(rowPos):
##            path += matrix[pos][pos]
##        if path <= pathValue:
##            pathValue = path
##
##        #check left negative diagonal
##        path = 0
##        for pos in range(1, rowPos + 1):
##            path += matrix[-pos][pos - 1]
##        if path <= pathValue:
##            pathValue = path

    return pathValue


def catAI(matrix, rowPos, colPos):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    nextMove = []

    pathValue = shortestPathValueCat(matrix, rowPos, colPos)
    print("PATHVALUE: ", pathValue)

    #check right path
    path = 0
    for col in range(colPos + 1, numColumns):
        path += matrix[rowPos][col]
    if path <= pathValue:
        nextMove += [[rowPos, colPos + 1]]

    #check left path
    path = 0
    for col in range(colPos):
        path += matrix[rowPos][col]
    if path <= pathValue:
        nextMove += [[rowPos, colPos - 1]]

    #check upper path
    path = 0
    for row in range(rowPos):
        path += matrix[row][colPos]
    if path <= pathValue:
        nextMove += [[rowPos - 1, colPos]]

    #check under path
    path = 0
    for row in range(rowPos + 1, numRows):
        path += matrix[row][colPos]
    if path <= pathValue:
        nextMove += [[rowPos + 1, colPos]]

##    if rowPos % 2 != 0:
##        #check right positive diagonal
##        path = 0
##        for pos in range(1, rowPos + 1):
##            path += matrix[pos - 1][-pos]
##        if path <= pathValue:
##            nextMove += [[rowPos - 1, colPos + 1]]
##
##        #check right negative diagonal
##        path = 0
##        for pos in range(rowPos + 1, numRows):
##            path += matrix[pos][pos]
##        if path <= pathValue:
##            nextMove += [[rowPos + 1, colPos + 1]]
##
##    if rowPos % 2 == 0:
##        #check left positive diagonal
##        path = 0
##        for pos in range(rowPos):
##            path += matrix[pos][pos]
##        if path <= pathValue:
##            nextMove += [[rowPos - 1, colPos - 1]]
##
##        #check left negative diagonal
##        path = 0
##        for pos in range(1, rowPos + 1):
##            path += matrix[-pos][pos - 1]
##        if path <= pathValue:
##            nextMove += [[rowPos + 1, colPos - 1]]        

    if pathValue >= 100:
        print("enter except")
        if rowPos % 2 != 0:
            nextMove = [[rowPos, colPos + 1], [rowPos, colPos - 1], [rowPos - 1, colPos], [rowPos + 1, colPos], [rowPos - 1, colPos + 1], [rowPos + 1, colPos + 1]]
        else:
            nextMove = [[rowPos, colPos + 1], [rowPos, colPos - 1], [rowPos - 1, colPos], [rowPos + 1, colPos], [rowPos - 1, colPos - 1], [rowPos + 1, colPos - 1]]

    print("CAT AI")            
    print(nextMove)
    return nextMove
        
        
matrixCat = [[5,5,5,5,5,5,5,5,5,5,5],
             [5,4,4,4,4,4,4,4,4,4,5],
             [5,4,3,3,3,3,3,3,3,4,5],
             [5,4,3,2,2,2,2,2,3,4,5],
             [5,4,3,2,1,1,1,2,3,4,5],
             [5,4,3,2,1,0,1,2,3,4,5],
             [5,4,3,2,1,1,1,2,3,4,5],
             [5,4,3,2,2,2,2,2,3,4,5],
             [5,4,3,3,3,3,3,3,3,4,5],
             [5,4,4,4,4,4,4,4,4,4,5],
             [5,5,5,5,5,5,5,5,5,5,5]]

matrixCat2 = [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
              [100, 4, 4, 4, 4, 4, 4, 4, 4, 4, 100],
              [100, 4, 3, 3, 3, 3, 3, 3, 3, 4, 100],
              [100, 4, 3, 2, 2, 2, 2, 2, 3, 4, 100],
              [100, 4, 3, 2, 1, 1, 1, 2, 3, 4, 100],
              [100, 4, 3, 2, 1, 0, 1, 2, 3, 4, 100],
              [100, 4, 3, 2, 1, 1, 1, 2, 3, 4, 100],
              [100, 4, 3, 2, 2, 2, 2, 2, 3, 4, 100],
              [100, 4, 3, 3, 3, 3, 3, 3, 3, 4, 100],
              [100, 4, 4, 4, 4, 4, 4, 4, 4, 4, 100],
              [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]



def makeMoveCat(matrix, orgRow, orgCol, storedValue):

    selectMove = pickValidMoveCat(matrix, catAI(matrix, orgRow, orgCol))
    nextRow = selectMove[0]
    nextCol = selectMove[1]
    

    matrix[orgRow][orgCol] = storedValue
    storedValue = matrix[nextRow][nextCol]
    matrix[nextRow][nextCol] = 0
    return [storedValue, [nextRow, nextCol]]


def pickValidMoveCat(matrix, nextMove):

    newNextMove = []
    
    for i in nextMove:
        nextRow = i[0]
        nextCol = i[1]
        if checkValidPositionCat(matrix, nextRow, nextCol):
            newNextMove += [i]
            
    print("NEXT MOVE")
    print(newNextMove)

    select = random.randrange(len(newNextMove))

    return newNextMove[select]


def checkValidPositionCat(matrix, nextRow, nextCol):

    if matrix[nextRow][nextCol] != 100 and matrix[nextRow][nextCol] != 0:
        return True
    else:
        return False


def winnerPlayerCat(matrix, rowPos, colPos):
    
    #check right path
    if matrix[rowPos][colPos + 1] == 100:
        #check left path
        if matrix[rowPos][colPos - 1] == 100:
            #check upper path
            if matrix[rowPos - 1][colPos] == 100:
                #check under path
                if matrix[rowPos + 1][colPos] == 100:
                    if rowPos % 2 != 0:
                        #check right positive diagonal
                        if matrix[rowPos - 1][colPos + 1] == 100:
                            #check negative diagonal
                            if matrix[rowPos + 1][colPos + 1] == 100:
                                return True
                    elif rowPos % 2 == 0:
                        if matrix[rowPos - 1][colPos - 1] == 100:
                            if matrix[rowPos + 1][colPos - 1] == 100:
                                return True
    return False

                        
def winnerCatAi(matrix, rowPos, colPos):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    nextMove = []

    if rowPos == 0 or rowPos == numRows - 1 or colPos == 0 or colPos == numColumns - 1:
        return True

    else:
        return False


def putPlayerPieceCat(matrix, row, col):

    if checkValidPositionCat(matrix, row, col):
        matrix[row][col] = 100
        return True
    else:
        return False


def createBoardCat(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    numBlocks = random.randrange(9, 14)

    i = 0
    while i < numBlocks:
        
        getRow = random.randrange(numRows)
        getCol = random.randrange(numColumns)
        
        if checkValidPositionCat(matrix, getRow, getRow):
            matrix[getRow][getCol] = 100
            i += 1

    return matrix
        


def startGameCat(player, playersCompleteInfo):

    gameOver = False

    matrix = [[5,5,5,5,5,5,5,5,5,5,5],
             [5,4,4,4,4,4,4,4,4,4,5],
             [5,4,3,3,3,3,3,3,3,4,5],
             [5,4,3,2,2,2,2,2,3,4,5],
             [5,4,3,2,1,1,1,2,3,4,5],
             [5,4,3,2,1,0,1,2,3,4,5],
             [5,4,3,2,1,1,1,2,3,4,5],
             [5,4,3,2,2,2,2,2,3,4,5],
             [5,4,3,3,3,3,3,3,3,4,5],
             [5,4,4,4,4,4,4,4,4,4,5],
             [5,5,5,5,5,5,5,5,5,5,5]]

    matrix = createBoardCat(matrix)
    
    widthDisplay = 930
    heightDisplay = 930
    
    numRows = len(matrix)
    numColumns = len(matrix[0])

    catDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    catPosRow = numRows//2
    catPosCol = numColumns//2

    storedValue = 1    #valor de la casilla a la que se movio el "gato"
    
    catDisplay.blit(backgroundImage, (0,0))
    drawBoardCat(matrix, catDisplay, widthDisplay, heightDisplay, backgroundImage)
    pygame.display.update()  

    while not gameOver:
                   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if inArea(0,0, 900, 900, catDisplay):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    posx = event.pos[0]
                    posy = event.pos[1]

                    posForX = 80
                    posForY = 80
                    
                    row = int(math.floor(posy/ posForY))

                    if row % 2 == 0:
                        column = int(math.floor(posx/ posForX))
                    if row % 2 != 0:
                        column = int(math.floor((posx - 35)/ posForY))

                    if putPlayerPieceCat(matrix, row, column):
                        drawBoardCat(matrix, catDisplay, widthDisplay, heightDisplay, backgroundImage)
                        pygame.display.update()
                        
                        if winnerCatAi(matrix, catPosRow, catPosCol):
                            gameOver = "AI"

                        elif winnerPlayerCat(matrix, catPosRow, catPosCol):
                            gameOver = "player"

                        else:
                            pygame.time.wait(250)
                            valuesList = makeMoveCat(matrix, catPosRow, catPosCol, storedValue)
                            storedValue = valuesList[0]
                            catPosRow = valuesList[1][0]
                            catPosCol = valuesList[1][1]
                            drawBoardCat(matrix, catDisplay, widthDisplay, heightDisplay, backgroundImage)

    pygame.time.wait(1000)
    if gameOver == "player":
        return "Gana"#winnerScreen(player, playersCompleteInfo, True)        
    else:
        return "Pierde"#winnerScreen(player, playersCompleteInfo, False) 

    


def drawBoardCat(matrix, screen, widthDisplay, heightDisplay, backgroundImage):

    global LIGHTGREEN, DARKGREEN, BLUE
    
    catImage = pygame.image.load("cat_viper.png")
    catImage = pygame.transform.scale(catImage, (70,70))

    radius = 35
    
    numRows = len(matrix)
    numColumns = len(matrix[0])
    
    screen.blit(backgroundImage, (0,0))
    pygame.display.update()
       
    for r in range(numRows):
        for c in range(numColumns):
            if r % 2 == 0: 
                posXmark = (c * (70+10)) + 10
                posYmark = (r * (70+10)) + 10

            if r % 2 != 0:
                posXmark = (c * (70+10)) + 45
                posYmark = (r * (70+10)) + 10                
                
            if matrix[r][c] != 0 and matrix[r][c] != 100:
                pygame.draw.circle(screen, LIGHTGREEN, (posXmark + radius, posYmark + radius), radius)
            if matrix[r][c] == 100:        
                pygame.draw.circle(screen, DARKGREEN, (posXmark + radius, posYmark + radius), radius)
            if matrix[r][c] == 0:        
#                screen.blit(catImage, (posXmark, posYmark))
                pygame.draw.circle(screen, BLUE, (posXmark + radius, posYmark + radius), radius)

    pygame.display.update()


def printMatrix(matrix):

    for i in matrix:
        print(*i)
