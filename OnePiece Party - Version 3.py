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





###########################################################################################################################################################



memoria1 = pygame.image.load("memoria1.png")
memoria2 = pygame.image.load("memoria2.png")
memoria3 = pygame.image.load("memoria3.png")
memoria4 = pygame.image.load("memoria4.png")
memoria5 = pygame.image.load("memoria5.png")
memoria6 = pygame.image.load("memoria6.png")
memoria7 = pygame.image.load("memoria7.png")
memoria8 = pygame.image.load("memoria8.png")
memoria9 = pygame.image.load("memoria9.png")

backCardMem = pygame.image.load("back_cardV2.png")

treasureChest = pygame.image.load("treasure_chest.png")
treasureChest = pygame.transform.scale(treasureChest, (90,85))


wantedLuffy = pygame.image.load("wanted_luffy.jpg")
wantedZoro = pygame.image.load("wanted_zoro.png")
wantedAce = pygame.image.load("wanted_ace.jpg")
wantedBoa = pygame.image.load("wanted_boa.jpg")
wantedBrook = pygame.image.load("wanted_brook.png")
wantedChopper = pygame.image.load("wanted_chopper.png")
wantedDoflamingo = pygame.image.load("wanted_doflamingo.jpg")
wantedFranky = pygame.image.load("wanted_franky.png")
wantedJinbe = pygame.image.load("wanted_jinbe.jpg")
wantedLaw = pygame.image.load("wanted_law.jpg")
wantedNami = pygame.image.load("wanted_nami.png")
wantedRobin = pygame.image.load("wanted_robin.png")
wantedSanji = pygame.image.load("wanted_sanji.png")
wantedSabo = pygame.image.load("wanted_sabo.png")
wantedUsopp = pygame.image.load("wanted_usopp.png")


luffyName = myFontSmall.render("Monkey D. Luffy", True, (69,69,69))
zoroName = myFontSmall.render("Roronoa Zoro", True, (69,69,69))
sanjiName = myFontSmall.render("Sanji Vinsmoke", True, (69,69,69))
namiName = myFontSmall.render("Nami", True, (69,69,69))
robinName = myFontSmall.render("Nico Robin", True, (69,69,69))
chopperName = myFontSmall.render("Tony Tony Chopper", True, (69,69,69))
brookName = myFontSmall.render("Brook", True, (69,69,69))
usoppName = myFontSmall.render("Usopp", True, (69,69,69))
frankyName = myFontSmall.render("Franky", True, (69,69,69))
jinbeName = myFontSmall.render("Jinbe", True, (69,69,69))
aceName = myFontSmall.render("Portgas D. Ace", True, (69,69,69))
boaName = myFontSmall.render("Boa Hancock", True, (69,69,69))
doflamingName = myFontSmall.render("Donquixote Doflamingo", True, (69,69,69))
saboName = myFontSmall.render("Sabo", True, (69,69,69))
lawName = myFontSmall.render("Trafalgar D. Law", True, (69,69,69))

backCardFlip = pygame.image.load("back_card2.png")
backCardFlip = pygame.transform.scale(backCardFlip, (200,250))

# luffyName, zoroName, sanjiName, namiName, robinName, chopperName, brookName, usoppName, frankyName, jinbeName, aceName, boaName, doflamingName, saboName, lawName      


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


###########################################################################################################################################################
################################################################### ASK FOR INPUT #########################################################################

#E: Ninguna
#S: Ninguna
#D: Retorna la tecla que se esta tocando en la ventana de Pygame
        
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass


#E: screen (ventana de pygame), message
#S: Ninguna
#D: Muestra el mensaje en medio de la ventana de pygame

def display_box(screen, message, x, y, color):
 # "Print a message in a box in the middle of the screen"
    
  global myFont
    
  if len(message) != 0:
    screen.blit(myFont.render(message, 1, (color)), (x, y))
  pygame.display.flip()


#E: screen, question (Lo que se quiere preguntar con el input
#S: Un string
#D: Retorna lo que se escribio en la cajita de "input"

def ask(screen, question, x, y, color):
  #"ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  string=''
  display_box(screen, question + ": " + string.join(current_string), x, y, color)
  while 1:
    inkey = get_key()
    if inkey == pygame.K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string), x, y, color)
  return string.join(current_string)

###########################################################################################################################################################


###########################################################################################################################################################
################################################################### TIC TAC TOE ###########################################################################


#E: 3 numeros, 1 matriz
#S: Boolean
#D: Agrega la pieza correspondiete si es valido

def addPieceTicTacToe(row, column, matrix, turn):

    if turn %2 == 0:
        if matrix[row][column] == "-":
            matrix[row][column] = "x"
            print(matrix)
            return True
    elif turn % 2 != 0:
        if matrix[row][column] == "-":
            matrix[row][column] = "0"
            print(matrix)
            return True

    return False


#E: 1 matriz, 1 string, screen, 2 numeros
#S: Boolean
#D: Retorna True si la pieza ingresada formo 3 en linea (gano en Tic Tac Toe). Ademas se dibuja una linea en la jugada ganadora

def winnerTicTacToe(matrix, piece, screen, widthDisplay, heightDisplay):

    global RED

    numRows = len(matrix)
    numColumns = len(matrix[0])

    #check horizontal winner
    for row in range(numRows):
        if matrix[row][0] == piece and matrix[row][1] == piece and matrix[row][2] == piece:
            pygame.draw.line(screen, RED, (0, (row * heightDisplay//3) + heightDisplay//6), (widthDisplay, (row * heightDisplay//3) + heightDisplay//6), 15)
            return True
        
    #check for vertical winner       
    for column in range(numColumns):
        if matrix[0][column] == piece and matrix[1][column] == piece and matrix[2][column] == piece:
            pygame.draw.line(screen, RED, ((column * widthDisplay//3) + widthDisplay//6, 0), ((column * widthDisplay//3) + widthDisplay//6, heightDisplay), 15)
            return True
    #check for left-to-right diagonal     
    if matrix[0][0] == piece:
        if matrix[1][1] == piece:
            if matrix[2][2] == piece:
                pygame.draw.line(screen, RED, (0,0), (widthDisplay, heightDisplay), 15)
                return True

    #check for right-to-left diagonal       
    if matrix[0][2] == piece:
        if matrix[1][1] == piece:
            if matrix[2][0] == piece:
                pygame.draw.line(screen, RED, (0, heightDisplay), (widthDisplay,0), 15)
                return True
            
    pygame.display.update()
    
    return False


def empateTicTacToe(matrix):

    for i in matrix:
        for j in i:
            if j == "-":
                return False

    return True
        
    
#E: una lista y un diccionario
#S: ninguna
#D: Funcion que inicia el juego de Tic Tac Toe

def startGameTicTacToe(players, playersCompleteInfo):

    global BLACK, GRAY, RED, myFontLarge

    player1 = players[0]
    player2 = players[1]

    matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    turn = 0
    
    gameOver = False

    widthDisplay = 1000
    heightDisplay = 960
    
    posForX = widthDisplay//3
    posForY = heightDisplay//3

    ticTacToeDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()

    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    while not gameOver:

        ticTacToeDisplay.blit(backgroundImage, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pygame.draw.line(ticTacToeDisplay, BLACK, (widthDisplay//3,0), (widthDisplay//3, heightDisplay), 5)
            pygame.draw.line(ticTacToeDisplay, BLACK, ((widthDisplay//3)*2,0), ((widthDisplay//3)*2, heightDisplay), 5)
            pygame.draw.line(ticTacToeDisplay, BLACK, (0,heightDisplay//3), (widthDisplay, heightDisplay//3), 5)
            pygame.draw.line(ticTacToeDisplay, BLACK, (0,(heightDisplay//3)*2), (widthDisplay,(heightDisplay//3)*2), 5)

                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                
                if turn % 2 == 0:
                    column = int(math.floor(posx/ posForX))
                    row = int(math.floor(posy/ posForY))
                    print("This is col:", column)
                    print("This is row:", row)
                    if addPieceTicTacToe(row, column, matrix, turn):
                        if winnerTicTacToe(matrix, "x", ticTacToeDisplay, widthDisplay, heightDisplay) == True:
                            print()
                            print("x Wins!!!")
                            winnerPl = player1
                            gameOver = True
                        turn += 1
                else:
                    column = int(math.floor(posx/ posForX))
                    row = int(math.floor(posy/ posForY))
                    if addPieceTicTacToe(row, column, matrix, turn):
                        if winnerTicTacToe(matrix, "0", ticTacToeDisplay, widthDisplay, heightDisplay) == True:
                            print()
                            print("0 Wins!!!")
                            winnerPl = player2
                            gameOver = True
                        turn += 1

        drawTicTacToe(matrix, ticTacToeDisplay, widthDisplay, heightDisplay)

        if empateTicTacToe(matrix):
            empateMsg = myFontLarge.render(("TIE"), True, (BLACK))
            ticTacToeDisplay.blit(empateMsg, (widthDisplay//3, heightDisplay//3))
            pygame.display.update()
            pygame.time.wait(1000)
            return startGameTicTacToe(players, playersCompleteInfo)
        
        pygame.display.update()

    if gameOver:
        pygame.time.wait(3500)
        if winnerPl == player1:
            return winnerScreen(winnerPl, playersCompleteInfo, True)
        else:
            return winnerScreen(player1, playersCompleteInfo, False)
            




def winnerScreen(playerName, playersCompleteInfo, win):

    global myFontLarge
    
    widthDisplay = 1500
    heightDisplay = 960

    posForX = widthDisplay//3
    posForY = heightDisplay//3


    winnerDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("winner_screen_background.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    winnerPlayer = myFontLarge.render((playerName + " WINS !!!!"), True, (69,69,69))
    loserPlayer = myFontLarge.render((playerName + " LOSES"), True, (69,69,69))

    playerPiece = playersCompleteInfo[playerName][1]
    pygame.time.wait(1000)

    inScreen = True

    iniTime = time.time()
    timer = 0
    maxTime = 6           #Tiempo maximo para el juego en segundos
    while timer < maxTime:
        endTime = time.time()
        timer = endTime - iniTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                timer = maxTime
        
        winnerDisplay.blit(backgroundImage, (0,0))
        winnerDisplay.blit(playerPiece, (300,200))
        if win:
            winnerDisplay.blit(winnerPlayer, (250, 100))
        elif not win:
            winnerDisplay.blit(loserPlayer, (250, 100))
        
        pygame.display.update()
    
    return win

    

#E: board, numRows, numColumns, screen
#S: Ninguna
#D: Dibuja el tablero (matrix) en una ventana de Pygame
                        
def drawTicTacToe(board, screen, widthDisplay, heightDisplay):

    global BLUE, GRAY, RED, YELLOW, BLACK, x_markIcon, o_markIcon

    SQUARESIZE = 100

    numRows = len(board)
    numColumns = len(board[0])

    posXmark = (widthDisplay//3)
    posYmark = (heightDisplay//3)
        
    pygame.draw.line(screen, BLACK, (widthDisplay//3,0), (widthDisplay//3, heightDisplay), 5)
    pygame.draw.line(screen, BLACK, ((widthDisplay//3)*2,0), ((widthDisplay//3)*2, heightDisplay), 5)
    pygame.draw.line(screen, BLACK, (0,heightDisplay//3), (widthDisplay, heightDisplay//3), 5)
    pygame.draw.line(screen, BLACK, (0,(heightDisplay//3)*2), (widthDisplay,(heightDisplay//3)*2), 5)
    
    for c in range(numColumns):
        for r in range(numRows):
            posXmark = (c*(widthDisplay//3)) + widthDisplay//15
            posYmark = r*(heightDisplay//3) + heightDisplay//15            
            if board[r][c] == "x":
                    screen.blit(x_markIcon, (int(posXmark), int(posYmark)))
            elif board[r][c] == "0": 
                    screen.blit(o_markIcon, (int(posXmark), int(posYmark)))
    pygame.display.update()


##def drawWinningLineTic(matrix, screen, piece, widthDisplay, heightDisplay):
##
##    global RED
##
##    numRows = len(matrix)
##    numColumns = len(matrix[0])
##
##    #check horizontal winner
##    for row in range(numRows):
##        if matrix[row][0] == piece and matrix[row][1] == piece and matrix[row][2] == piece:
##            pygame.draw.line(screen, RED, (0, (row * heightDisplay//3) + heightDisplay//6), (widthDisplay, (row * heightDisplay//3) + heightDisplay//6), 15)
##
##    #check for vertical winner       
##    for column in range(numColumns):
##        if matrix[0][column] == piece and matrix[1][column] == piece and matrix[2][column] == piece:
##            pygame.draw.line(screen, RED, ((column * widthDisplay//3) + widthDisplay//6, 0), ((column * widthDisplay//3) + widthDisplay//6, heightDisplay), 15)
##
##    #check for left-to-right diagonal     
##    if matrix[0][0] == piece:
##        if matrix[1][1] == piece:
##            if matrix[2][2] == piece:
##                pygame.draw.line(screen, RED, (0,0), (widthDisplay, heightDisplay), 15)
##
##    #check for right-to-left diagonal       
##    if matrix[0][2] == piece:
##        if matrix[1][1] == piece:
##            if matrix[2][0] == piece:
##                pygame.draw.line(screen, RED, (0, heightDisplay), (widthDisplay,0), 15)
##            
##    pygame.display.update()
##    


###########################################################################################################################################################
################################################################## GUESS THE PATH #########################################################################

emptyMatrix = [[0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]

def createPath(matrix):

    numColumns = len(matrix[0])
    
    for row in matrix:
        column = random.randrange(numColumns)
        row[column] = 1

    return matrix

def openChestPath(matrix, row, column, path):

    if row == path:
        if matrix[row][column] == 1:
            matrix[row][column] = 2
            print("open")
            print(matrix)
            return 1
        else:
            return 2
        
    return

def winnerGsThePath(matrix):
    
    counter = 0
    
    for row in matrix:
        if 2 in row:
            counter += 1

    if counter >= 8:
        return True
    return False

def startGameGsThePath(playerName, playersCompleteInfo):

    matrix = formMatrix(8,3)

    matrix = createPath(matrix)
    
    return gsThePathGame(matrix, playerName, playersCompleteInfo)

#TAMAÑO DE MATRIZ = 8x3

def gsThePathGame(matrix, player, playersCompleteInfo, lives = 5, path = 7):

    global BLACK, GRAY, RED

    gameOver = False

    widthDisplay = 800
    heightDisplay = 960
    
    posForX = widthDisplay//6
    posForY = heightDisplay//8

    gsThePathDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    originalMatrix = [x[:] for x in matrix]

    while not gameOver:

        gsThePathDisplay.blit(backgroundImage, (0,0))      

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            print("lives:", lives)
            print("path: ", path)

            if inArea(400,25, 400, 935, gsThePathDisplay):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    posy = event.pos[1]                
                    if lives > 0:
                        column = int(math.floor(posx/ posForX)) - 3
                        row = int(math.floor(posy/ posForY))
                        if openChestPath(matrix, row, column, path) == 1:
                            path -= 1
                        if openChestPath(matrix, row, column, path) == 2:
                            return gsThePathGame(originalMatrix, player, playersCompleteInfo, lives - 1, 7)

        drawBoardGsThePath(matrix, gsThePathDisplay, widthDisplay, heightDisplay, lives)

        pygame.display.update()

        if lives == 0:
            win = False
            gameOver = True
            

        if path == -1:
            win = True
            gameOver = True
            
    if gameOver:
        pygame.time.wait(3500)
        if win:
            return winnerScreen(player, playersCompleteInfo, True)
        else:
            return winnerScreen(player, playersCompleteInfo, False)
        

def drawBoardGsThePath(board, screen, widthDisplay, heightDisplay, lives):

    global BLUE, GRAY, RED, YELLOW, BLACK, x_markIcon, o_markIcon, treasureChest

    goldPile = pygame.image.load("pile_of_gold.png")
    goldPile = pygame.transform.scale(goldPile, (90,85))

    keyIcon = pygame.image.load("key_icon.png")
    keyIcon = pygame.transform.scale(keyIcon, (250,100))

    numRows = len(board)
    numColumns = len(board[0])

    posXmark = (widthDisplay//3)
    posYmark = (heightDisplay//3)
        
    for c in range(numColumns):
        for r in range(numRows):
            posXmark = (c*(widthDisplay//6)) + widthDisplay//2
            posYmark = r*(heightDisplay//8) + heightDisplay//30            
            if board[r][c] == 0:
                screen.blit(treasureChest, (int(posXmark), int(posYmark)))
            elif board[r][c] == 1: 
                screen.blit(treasureChest, (int(posXmark), int(posYmark)))
            elif board[r][c] == 2:
                screen.blit(goldPile, (int(posXmark), int(posYmark)))

    for key in range(lives):

        posKeyY = (key * 150) + 100
        
        screen.blit(keyIcon, (75, int(posKeyY)))
        
    
    pygame.display.update()


###########################################################################################################################################################
###################################################################### MEMORY #############################################################################
    
memMatrx = [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]


def getRandomNum(range):

    num = random.randrange(range)

    return num


def createBoardMemory(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    figure = 9
    
    while figure > 0:

        counter = 0
        
        row1 = random.randrange(numRows)
        row2 = random.randrange(numRows)
        column1 = random.randrange(numColumns)
        column2 = random.randrange(numColumns)

        for i in range(numRows):
            for j in range(numColumns):
                if matrix[i][j] == figure:
                    counter += 1

        if counter == 0:
            if matrix[row1][column1] == 0:
                matrix[row1][column1] = figure
        
        if counter == 1:        
            if matrix[row2][column2] == 0:
                matrix[row2][column2] = figure

        if counter == 2:
            figure -= 1

    print("Final")
    printMatrix(matrix)
    return matrix


#TAMAÑO DE MATRIZ = 3x6

def startGameMemory(players, playersCompleteInfo):

    global BLACK, GRAY, RED

    player1 = players[0]
    player2 = players[1]

    lowerMatrix = formMatrix(3,6)
    upperMatrix = formMatrix(3,6)

    gameOver = False

    widthDisplay = 1300
    heightDisplay = 960
    
    posForX = widthDisplay//6 
    posForY = heightDisplay//4

    memoryDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    turn = 0

    lowMatCopy = [x[:] for x in lowerMatrix]

    player1Points = 0
    player2Points = 0

    upperMatrix = createBoardMemory(upperMatrix)

    playerChos = 1
    
    playerTurn = myFont.render("Player 1", True, (69,69,69))

    while not gameOver:

        memoryDisplay.blit(backgroundImage, (0,0))      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if inArea(0,0, widthDisplay, (heightDisplay//4) * 3, memoryDisplay):
                
                if turn == 0:
                    playerTurn = myFont.render("Player " + str(players[playerChos-1]), True, (69,69,69))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        posy = event.pos[1]                
                        column1 = int(math.floor(posx/ posForX))
                        row1 = int(math.floor(posy/ posForY))
                        print("Row1:", row1)
                        print("Col1:", column1)
                        print(lowerMatrix)
                        if revealFigureMemory(lowerMatrix, row1, column1, 1):
                            drawBoardMemory(lowerMatrix, upperMatrix, memoryDisplay, widthDisplay, heightDisplay, playerTurn)
                            pygame.display.update()
                            turn = 1

                if turn == 1:
                    playerTurn = myFont.render("Player " + str(players[playerChos-1]), True, (69,69,69))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        posy = event.pos[1]                
                        column2 = int(math.floor(posx/ posForX))
                        row2 = int(math.floor(posy/ posForY))
                        print("Row2:", row2)
                        print("Col2:", column2)
                        
                        if revealFigureMemory(lowerMatrix, row2, column2, 1):
                            drawBoardMemory(lowerMatrix, upperMatrix, memoryDisplay, widthDisplay, heightDisplay, playerTurn)
                            pygame.display.update()

                            pygame.time.wait(1000)
                            print(lowerMatrix)
                            if checkPairMemory(upperMatrix, row1, column1, row2, column2):
                                lowMatCopy = [x[:] for x in lowerMatrix]
                                if playerChos == 1:
                                    player1Points += 1
                                if playerChos == 2:
                                    player2Points += 1
                                    
                                turn = 0

                            else:
                                lowerMatrix = [x[:] for x in lowMatCopy]
                                if playerChos == 1:
                                    playerChos = 2
                                else:
                                    playerChos = 1
                                        
                                turn = 0
                                
                            drawBoardMemory(lowerMatrix, upperMatrix, memoryDisplay, widthDisplay, heightDisplay, playerTurn)
                            pygame.display.update()


            drawBoardMemory(lowerMatrix, upperMatrix, memoryDisplay, widthDisplay, heightDisplay, playerTurn)
            pygame.display.update()

        gameOver = gameOverMemory(lowerMatrix)
            
    if gameOver:
        pygame.time.wait(3500)
        if player1Points > player2Points:            
            return winnerScreen(player1, playersCompleteInfo, True)
        else:
            return winnerScreen(player1, playersCompleteInfo, False)


def revealFigureMemory(matrix, row, column, piece):

    if matrix[row][column] == 0:
        matrix[row][column] = piece
        return True

    return False


def gameOverMemory(lowerMatrix):

    for i in lowerMatrix:
        if 0 in i:
            return False
    else:
        return True


def checkPairMemory(matrix, row1, column1, row2, column2):

    if matrix[row1][column1] == matrix[row2][column2]:
        return True
    else:
        return False    



    

def drawBoardMemory(lowerMatrix, upperMatrix, screen, widthDisplay, heightDisplay, playerTurn):

    global memoria1, memoria2, memoria3, memoria4, memoria5, memoria6, memoria7, memoria8, memoria9

    pieceSize = 190

    memoria1 = pygame.transform.scale(memoria1, (pieceSize,pieceSize))
    memoria2 = pygame.transform.scale(memoria2, (pieceSize,pieceSize))
    memoria3 = pygame.transform.scale(memoria3, (pieceSize,pieceSize))
    memoria4 = pygame.transform.scale(memoria4, (pieceSize,pieceSize))
    memoria5 = pygame.transform.scale(memoria5, (pieceSize,pieceSize))
    memoria6 = pygame.transform.scale(memoria6, (pieceSize,pieceSize))
    memoria7 = pygame.transform.scale(memoria7, (pieceSize,pieceSize))
    memoria8 = pygame.transform.scale(memoria8, (pieceSize,pieceSize))
    memoria9 = pygame.transform.scale(memoria9, (pieceSize,pieceSize))

    figuresList = ["offset", memoria1, memoria2, memoria3, memoria4, memoria5, memoria6, memoria7, memoria8, memoria9]

    backCardMem = pygame.image.load("back_cardV2.png")
    backCardMem = pygame.transform.scale(backCardMem, (pieceSize,pieceSize))

    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])

    screen.blit(playerTurn, (widthDisplay//2,870))
        
    for c in range(numColumns):
        for r in range(numRows):
            posXmark = (c*(widthDisplay//6)) + 15 
            posYmark = r*(heightDisplay//4) + 15       
            if lowerMatrix[r][c] == 0:
                screen.blit(backCardMem, (int(posXmark), int(posYmark)))
            elif lowerMatrix[r][c] == 1:
                showFigure = figuresList[upperMatrix[r][c]]
                screen.blit(showFigure, (int(posXmark), int(posYmark)))
            elif lowerMatrix[r][c] == 2:
                showFigure = figuresList[upperMatrix[r][c]]
                screen.blit(showFigure, (int(posXmark), int(posYmark)))
    
    
    pygame.display.update()


###########################################################################################################################################################
############################################################### COLLECT THE TREASURE ######################################################################


def createBoardColTheTrea(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    positiveNums = (numRows * numColumns) // 2
    negativeNums = (numRows * numColumns) // 2

    while negativeNums > 0:

        row = random.randrange(numRows)
        column = random.randrange(numColumns)

        value = -(random.randrange(1,10))

        if matrix[row][column] == 0:
            matrix[row][column] = value
            negativeNums -= 1
        
    while positiveNums > 0:

        row = random.randrange(numRows)
        column = random.randrange(numColumns)

        value = random.randrange(1,10)

        if matrix[row][column] == 0:
            matrix[row][column] = value
            positiveNums -= 1

    return matrix


def startGameColTheTrea(player, playersCompleteInfo):

    global BLACK, GRAY, RED

    lowerMatrix = formMatrix(6,7)
    upperMatrix = formMatrix(6,7)

    gameOver = False

    widthDisplay = 1300
    heightDisplay = 960
    
    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])

    posForX = widthDisplay//numColumns
    posForY = heightDisplay//numRows

    colTheTreasureDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    turn = 9

    lowMatCopy = [x[:] for x in lowerMatrix]

    player1Points = 0

    upperMatrix = createBoardColTheTrea(upperMatrix)
    
    playerTurn = myFont.render(("Turn # " + str(turn)), True, (69,69,69))
    score = myFont.render(("SCORE: " + str(player1Points)), True, (69,69,69))

    while not gameOver:

        colTheTreasureDisplay.blit(backgroundImage, (0,0))      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if inArea(0,0, 1300, 960, colTheTreasureDisplay):
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        posy = event.pos[1]                
                        column = int(math.floor(posx/ posForX))
                        row = int(math.floor(posy/ posForY))
    ##                    print("Row:", row1)
    ##                    print("Col:", column1)
                        
                        if revealFigureMemory(lowerMatrix, row, column, 1):
                            print(lowerMatrix)
                            drawBoardColTheTrea(lowerMatrix, upperMatrix, colTheTreasureDisplay, widthDisplay, heightDisplay, playerTurn, score)
                            pygame.display.update()
                            
                            turn -= 1

                            player1Points += upperMatrix[row][column]

        playerTurn = myFont.render(("Turn # " + str(turn)), True, (69,69,69))
        score = myFont.render(("SCORE: " + str(player1Points)), True, (69,69,69))
        drawBoardColTheTrea(lowerMatrix, upperMatrix, colTheTreasureDisplay, widthDisplay, heightDisplay, playerTurn, score)
        pygame.display.update()        

        if turn == 0:
            colTheTreasureDisplay.blit(backgroundImage, (0,0))
            playerTurn = myFont.render(("Turn # " + str(turn)), True, (69,69,69))
            score = myFont.render(("SCORE: " + str(player1Points)), True, (69,69,69))
            drawBoardColTheTrea(lowerMatrix, upperMatrix, colTheTreasureDisplay, widthDisplay, heightDisplay, playerTurn, score)
            pygame.display.update()        
            gameOver = True

    if gameOver:
        pygame.time.wait(3500) 
        if player1Points > 0:
            return winnerScreen(player, playersCompleteInfo, True)
        else:
            return winnerScreen(player, playersCompleteInfo, False)
        


def drawBoardColTheTrea(lowerMatrix, upperMatrix, screen, widthDisplay, heightDisplay, playerTurn, score):

    global treasureChest

    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])
    

    screen.blit(playerTurn, (widthDisplay//2,870))
    screen.blit(score, (widthDisplay//4,870))
        
    for c in range(numColumns):
        for r in range(numRows):
            posXmark = (c*(widthDisplay//numColumns))
            posYmark = r*(heightDisplay//numRows)      
            if lowerMatrix[r][c] == 0:
                screen.blit(treasureChest, (int(posXmark), int(posYmark)))
            elif lowerMatrix[r][c] == 1:
                showNum = upperMatrix[r][c]
                showNum = myFont.render(str(showNum), True, (69,69,69))
                screen.blit(showNum, (int(posXmark), int(posYmark)))
    
    
    pygame.display.update()


def openChestColTheTrea(matrix, row, col):

    if matrix[row][col] == 0:
        matrix[row][col] = 1
        return True
    else:
        return False




###########################################################################################################################################################
########################################################################## GUESS WHO ######################################################################


def makeClueGsWho(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    
    spaces = random.randrange(6,11)

    while spaces > 0:
        row = random.randrange(numRows)
        col = random.randrange(numColumns)

        if matrix[row][col] == 0:
            matrix[row][col] = 1
            spaces -= 1

    return matrix


def startGameGsWho(player, playersCompleteInfo):

    global wantedLuffy, wantedZoro, wantedAce, wantedBoa, wantedBrook, wantedChopper, wantedDoflamingo, wantedFranky, wantedJinbe, wantedLaw, wantedNami, wantedRobin, wantedSanji, wantedSabo, wantedUsopp
    global luffyName, zoroName, sanjiName, namiName, robinName, chopperName, brookName, usoppName, frankyName, jinbeName, aceName, boaName, doflamingName, saboName, lawName, myFont

    matrix = formMatrix(10,9)
    
    characterList = [wantedLuffy, wantedZoro, wantedSanji, wantedNami, wantedRobin, wantedChopper, wantedBrook, wantedUsopp, wantedFranky, wantedJinbe, wantedAce, wantedBoa, wantedDoflamingo, wantedSabo, wantedLaw]
    namesList = [luffyName, zoroName, sanjiName, namiName, robinName, chopperName, brookName, usoppName, frankyName, jinbeName, aceName, boaName, doflamingName, saboName, lawName]

    charNum = random.randrange(15)
    character = characterList[charNum]
    
    matrix = makeClueGsWho(matrix)

    gameOver = False

    widthDisplay = 1300
    heightDisplay = 960
    
    numRows = len(matrix)
    numColumns = len(matrix[0])

    posForX = widthDisplay//numColumns
    posForY = heightDisplay//numRows

    gsWhoDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    lives = 3
    
    gsWhoDisplay.blit(backgroundImage, (0,0))
    drawBoardGsWho(matrix, character, gsWhoDisplay, widthDisplay, heightDisplay)

    for i in range(1,16):
        showName = namesList[i - 1]
        gsWhoDisplay.blit(showName, (960, 60 * i))
    
    pygame.display.update()

    posy = 0

# 960, 65
    while not gameOver:

        livesLeftMsg = myFont.render(("lives: " + str(lives)), True, (69,69,69))
        gsWhoDisplay.blit(backgroundImage, (0,0))
        drawBoardGsWho(matrix, character, gsWhoDisplay, widthDisplay, heightDisplay)
        
        for i in range(1,16):
            showName = namesList[i - 1]
            gsWhoDisplay.blit(showName, (960, 60 * i))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                
            if inArea(960,0, 1300-960, 960, gsWhoDisplay):
                posy = pygame.mouse.get_pos()
                posy = posy[1]
                posy = posy//60 
            
 
        if buttonInGame(960,60*posy, 100, 40, gsWhoDisplay, 200, 5):
            if charNum + 1 == posy:
                win = True
                gameOver = True
            else:
                lives -= 1

        if lives == 0:
            win = False
            gameOver = True

        livesLeftMsg = myFont.render(("lives: " + str(lives)), True, (69,69,69))
        gsWhoDisplay.blit(livesLeftMsg, (0,0))
        pygame.display.update()
                
    if gameOver:
        pygame.time.wait(3500)
        if win:
            return winnerScreen(player, playersCompleteInfo, True)
        else:
            return winnerScreen(player, playersCompleteInfo, False)



def showTheButton(xPos, yPos, width, height, screen, moveRight, moveDown):

    buttonInGame(xPos, yPos, width, height, screen, moveRight, moveDown)


def drawBoardGsWho(matrix, character, screen, widthDisplay, heightDisplay):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    pieceSize = 100
    backCardMem = pygame.image.load("back_cardV2.png")
    backCardMem = pygame.transform.scale(backCardMem, (pieceSize,pieceSize))
    
    character = pygame.transform.scale(character, ((widthDisplay//3)*2,heightDisplay))

    screen.blit(character, (0,0))

    for c in range(numColumns):
        for r in range(numRows):
            posXmark = (c*(pieceSize))
            posYmark = r*(heightDisplay//numRows)      
            if matrix[r][c] == 0:
                screen.blit(backCardMem, (int(posXmark), int(posYmark)))    
    
    pygame.display.update()    



###########################################################################################################################################################
########################################################################## FLIP CARDS ######################################################################

        
path_to_directory = "D:\\Users\Joaquin\\Documents\\Joaquin Uni\\TEC\Intro y Taller\\Proyecto 3\\PNG"

def load_images(path_to_directory):
    """Load images and return them as a dict."""
    image_dict = {}
    for filename in os.listdir(path_to_directory):
        if filename.endswith('.png'):
            path = os.path.join(path_to_directory, filename)
            key = filename[:-4]
            image_dict[key] = pygame.image.load(path).convert()
    return image_dict


def shuffleCardsMatrix(cardsList, numRows, numColumns):

    keyMatrix = []
    for i in range(numRows):
        newRow = []
        for j in range(numColumns):
            newRow += [cardsList[i*numColumns + j]]
        keyMatrix += [newRow]
    return keyMatrix
    
def startGameFlipCards(playerName, playerList, playersCompleteInfo):

    gameOver = False

    widthDisplay = 1480
    heightDisplay = 960

    numRows = 3
    numColumns = 7
    
    posForX = 210
    posForY = 260

    flipCardsDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    cardsPack = load_images(path_to_directory)

    keyList = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'EC', 'ED', 'EH', 'ES', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS', 'ZAC', 'ZAD', 'ZAH', 'ZAS']
    random.shuffle(keyList)
    keyMatrix = shuffleCardsMatrix(keyList, numRows, numColumns)

    lowerMatrix = formMatrix(numRows, numColumns)

    turn = 0

    playersCards = []
    
##    playerTurn = myFont.render(("Turn # " + str(turn)), True, (69,69,69))
##    score = myFont.render(("SCORE: " + str(player1Points)), True, (69,69,69))      
    playerTurn = myFont.render(("Player " + str(playerList[turn])), True, (69,69,69))
    drawBoardCards(lowerMatrix, keyMatrix, flipCardsDisplay, widthDisplay, heightDisplay, cardsPack, playerTurn, backgroundImage)
    pygame.display.update()    

    while not gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        if inArea(0,0, 1470, 780, flipCardsDisplay):
            
##                    playerTurn = myFont.render(("Turn # " + str(turn)), True, (69,69,69))
##                    score = myFont.render(("SCORE: " + str(player1Points)), True, (69,69,69))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    posy = event.pos[1]                
                    column = int(math.floor(posx/ posForX))
                    row = int(math.floor(posy/ posForY))
                    
                    if revealFigureMemory(lowerMatrix, row, column, 1):
                        print(lowerMatrix)                        
                        
                        turn += 1
                        
                        playersCards += [keyMatrix[row][column]]

                        drawBoardCards(lowerMatrix, keyMatrix, flipCardsDisplay, widthDisplay, heightDisplay, cardsPack, playerTurn, backgroundImage)

        if turn == len(playerList):
            gameOver = True

        else:
            playerTurn = myFont.render(("Player " + str(playerList[turn])), True, (69,69,69))
            drawBoardCards(lowerMatrix, keyMatrix, flipCardsDisplay, widthDisplay, heightDisplay, cardsPack, playerTurn, backgroundImage)
        
    if gameOver:
        winnerCard = max(playersCards)
        winnerPlayer = playerList[getListPosition(winnerCard, playersCards)]
        pygame.time.wait(3500)
        if winnerPlayer == playerName:
            return winnerScreen(playerName, playersCompleteInfo, True)
        else:
            return winnerScreen(playerName, playersCompleteInfo, False)
    

def getListPosition(elem, lista):

    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def drawBoardCards(lowerMatrix, keyMatrix, screen, widthDisplay, heightDisplay, cardsPack, playerTurn, backgroundImage):

    global backCardFlip

    numRows = len(keyMatrix)
    numColumns = len(keyMatrix[0])

    screen.blit(backgroundImage, (0,0))
       
    for r in range(numRows):
        for c in range(numColumns):
            posXmark = (c * 210) + 10
            posYmark = (r * 260) + 10 
            if lowerMatrix[r][c] != 0:        
                image = cardsPack.get(keyMatrix[r][c])
                image = pygame.transform.scale(image, (200,250))
                screen.blit(image, (posXmark, posYmark))
            else:
                screen.blit(backCardFlip, (posXmark, posYmark))

    screen.blit(playerTurn, (widthDisplay//2, 890))                
    pygame.display.update()
    


###########################################################################################################################################################
############################################################################ BOMBER #######################################################################


def createBoardBomber(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])
    
    row = random.randrange(numRows) 
    col = random.randrange(numColumns)

    if row < numRows - 1 and col < numColumns - 1:
        matrix[row][col] = 1
        matrix[row][col + 1] = 1
        matrix[row + 1][col] = 1
        matrix[row + 1][col + 1] = 1
        return matrix
        
    elif row == numRows - 1 and col < numColumns - 1:
        matrix[row][col] = 1
        matrix[row][col + 1] = 1
        matrix[row - 1][col] = 1
        matrix[row - 1][col + 1] = 1
        return matrix

    elif row == 0 and col == numColumns - 1:        
        matrix[row][col] = 1
        matrix[row][col - 1] = 1
        matrix[row + 1][col] = 1
        matrix[row + 1][col - 1] = 1
        return matrix
    
    else:
        matrix[row][col] = 1
        matrix[row][col - 1] = 1
        matrix[row - 1][col] = 1
        matrix[row - 1][col - 1] = 1
        return matrix    


def revealSpaceBomber(matrix, row, col):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    if matrix[row][col] == 0:
        if row < numRows - 1 and col < numColumns - 1:
            matrix[row][col] = 1
            matrix[row][col + 1] = 1
            matrix[row + 1][col] = 1
            matrix[row + 1][col + 1] = 1
            return True
            
        elif row == numRows - 1 and col < numColumns - 1:
            matrix[row][col] = 1
            matrix[row][col + 1] = 1
            matrix[row - 1][col] = 1
            matrix[row - 1][col + 1] = 1
            return True
        
        elif row == 0 and col == numColumns - 1:        
            matrix[row][col] = 1
            matrix[row][col - 1] = 1
            matrix[row + 1][col] = 1
            matrix[row + 1][col - 1] = 1
            return True

        else:
            matrix[row][col] = 1
            matrix[row][col - 1] = 1
            matrix[row - 1][col] = 1
            matrix[row - 1][col - 1] = 1
            return True
    else:
        return False


def winnerBomber(lowerMatrix, upperMatrix):

    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])
    
    for row in range(numRows):
        for col in range(numColumns):
            if row < numRows - 1 and col < numColumns - 1:
                if lowerMatrix[row][col] == 1 and lowerMatrix[row][col + 1] == 1 and lowerMatrix[row + 1][col] == 1 and lowerMatrix[row + 1][col + 1] == 1:
                    if upperMatrix[row][col] == 1 and upperMatrix[row][col + 1] == 1 and upperMatrix[row + 1][col] == 1 and upperMatrix[row + 1][col + 1] == 1:
                        return True
                        
            elif row == numRows - 1 and col < numColumns - 1:
                if lowerMatrix[row][col] == 1 and lowerMatrix[row][col + 1] == 1 and lowerMatrix[row - 1][col] == 1 and lowerMatrix[row - 1][col + 1] == 1:
                    if upperMatrix[row][col] == 1 and upperMatrix[row][col + 1] == 1 and upperMatrix[row - 1][col] == 1 and upperMatrix[row - 1][col + 1] == 1:
                        return True

            elif row == numRows - 1 and col < numColumns - 1:
                if lowerMatrix[row][col] == 1 and lowerMatrix[row][col - 1] == 1 and lowerMatrix[row + 1][col] == 1 and lowerMatrix[row + 1][col - 1] == 1:
                    if upperMatrix[row][col] == 1 and upperMatrix[row][col - 1] == 1 and upperMatrix[row + 1][col] == 1 and upperMatrix[row + 1][col - 1] == 1:
                        return True

            else:
                if lowerMatrix[row][col] == 1 and lowerMatrix[row][col - 1] == 1 and lowerMatrix[row - 1][col] == 1 and lowerMatrix[row - 1][col - 1] == 1:
                    if upperMatrix[row][col] == 1 and upperMatrix[row][col - 1] == 1 and upperMatrix[row - 1][col] == 1 and upperMatrix[row - 1][col - 1] == 1:
                        return True
    return False


def startGameBomber(player, playersCompleteInfo):

    version = random.randrange(3)

    if version == 0:
        return gameBomber(formMatrix(10,10), formMatrix(10,10), player, 75, playersCompleteInfo)

    elif version == 1:
        return gameBomber(formMatrix(15,15), formMatrix(15,15), player, 50, playersCompleteInfo)

    elif version == 2:
        return gameBomber(formMatrix(20,20), formMatrix(20,20), player, 35, playersCompleteInfo)
    

def gameBomber(lowerMatrix, upperMatrix, player1, spaceSize, playersCompleteInfo):

    global BLACK, GRAY, RED

    gameOver = False

    widthDisplay = 950
    heightDisplay = 1000
    
    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])

    posForX = spaceSize + 10
    posForY = spaceSize + 10

    bomberDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    lives = 10

    lowerMatrix = createBoardBomber(lowerMatrix)

    printMatrix(lowerMatrix)
    
    numBombs = myFont.render(("Bombs left: " + str(lives)), True, (69,69,69))

    bomberDisplay.blit(backgroundImage, (0,0))
    drawBoardBomber(lowerMatrix, upperMatrix, bomberDisplay, widthDisplay, heightDisplay, numBombs, backgroundImage, spaceSize)
    pygame.display.update()  

    while not gameOver:
                   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if inArea(0,0, 900, 900, bomberDisplay):
                
                    numBombs = myFont.render(("Bombs left: " + str(lives)), True, (69,69,69))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        posy = event.pos[1]                
                        column = int(math.floor(posx/ posForX))
                        row = int(math.floor(posy/ posForY))
                        print("Row:", row)
                        print("Col:", column)
                        
                        if revealSpaceBomber(upperMatrix, row, column):
                            drawBoardBomber(lowerMatrix, upperMatrix, bomberDisplay, widthDisplay, heightDisplay, numBombs, backgroundImage, spaceSize)
                            pygame.display.update()
                            
                            lives -= 1
                            numBombs = myFont.render(("Bombs left: " + str(lives)), True, (69,69,69))
                            if winnerBomber(lowerMatrix, upperMatrix):
                                lives = -1
            
        if lives <= 0:            
            drawBoardBomber(lowerMatrix, upperMatrix, bomberDisplay, widthDisplay, heightDisplay, numBombs, backgroundImage, spaceSize)
            pygame.display.update()
            gameOver = True

    if gameOver:
        pygame.time.wait(3500) 
        if lives < 0:
            return winnerScreen(player1, playersCompleteInfo, True)
        else:
            return winnerScreen(player1, playersCompleteInfo, False)



def drawBoardBomber(lowerMatrix, upperMatrix, screen, widthDisplay, heightDisplay, numBombs, backgroundImage, spaceSize):

    global backCardFlip

    numRows = len(upperMatrix)
    numColumns = len(upperMatrix[0])

    goldCoin = pygame.image.load("pile_of_gold.png")
    goldCoin = pygame.transform.scale(goldCoin, (spaceSize,spaceSize))

    backCard = pygame.image.load("back_cardV2.png")
    backCard = pygame.transform.scale(backCard, (spaceSize,spaceSize))

    bombIcon = pygame.image.load("bomb.png")
    bombIcon = pygame.transform.scale(bombIcon, (spaceSize,spaceSize))
    
    screen.blit(backgroundImage, (0,0))
    pygame.display.update()
       
    for r in range(numRows):
        for c in range(numColumns):
            posXmark = (c * (spaceSize+10)) + 10
            posYmark = (r * (spaceSize+10)) + 10
            if upperMatrix[r][c] != 0:
                if lowerMatrix[r][c] != 0:        
                    screen.blit(goldCoin, (posXmark, posYmark))
                    pygame.display.update()
                else:
                    screen.blit(bombIcon, (posXmark, posYmark))
                    pygame.display.update()
                    
            else:
                screen.blit(backCard, (posXmark, posYmark))
                pygame.display.update()


    screen.blit(numBombs, (widthDisplay//2, 890))                
    pygame.display.update()



###########################################################################################################################################################
###################################################################### CATCH THE CAT ######################################################################

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
        return winnerScreen(player, playersCompleteInfo, True)        
    else:
        return winnerScreen(player, playersCompleteInfo, False) 

    


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



def drawCircle():

    global DARKGREEN

    widthDisplay = 960
    heightDisplay = 960

    radius = 35
    
    catDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))
    catDisplay.blit(backgroundImage, (0,0))
    pygame.display.update()

    pygame.draw.circle(catDisplay, DARKGREEN, (0 +35, 0 +35), radius)
    pygame.display.update()
    

###########################################################################################################################################################
###################################################################### SOPA DE LETRAS #####################################################################


def createBoardSopa(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    wordsList = ["ABAJO", "DRAGON", "LENTO", "RAPIDO", "BARCO", "DIEGO", "CAMARON", "AVENIDA",
                 "EROSION", "LAPICERO", "BARCO", "PAPEL", "CONGRESO", "ABUELOS", "AFRICA",
                 "TIERRA", "MEDIA", "ENTIERRO", "COLORES", "BARRANCO", "CIENCIA", "VIVIR",
                 "VECINDARIO", "FRACASAR", "PROGRAMA", "MAPAS", "MUNDO", "PIRATAS", "CONGELADOR",
                 "BARRANCO", "MUERTE", "CEPILLO", "LIMPIEZA", "ESTUCHE", "CONTRUIR", "DERROTAR",
                 "FORJAR", "RECREO", "PRIMERO", "GOLOSINA", "SUFRAGIO", "TOSTADORA", "ESPOSA",
                 "BOTAS", "PROFESOR", "ENSEÑAR", "CHISTE", "FUTURO", "EMISION", "ORGANO",
                 "EMPAQUE", "TRAJE", "EQUIPO", "SELECCIÓN", "TENEDOR", "APAGON", "CONCAVO",
                 "PINTURA", "FISCAL", "PISCINA", "DESPIERTO", "JOVEN", "CONFUCIO", "ANIMAL",
                 "MILITAR", "EMPAPADO", "SILUETA", "FRACTURA", "PUERTO", "EXTRAER", "PRISION",
                 "TABLERO", "LENGUA", "ESCULPIR", "DESCANSO", "RUMOR", "ARTES", "PERCHA",
                 "ASALTO", "SERVICIO", "FUNCION", "ESCRITORIO", "TECLADO", "ESCONDER", "ISLAS",
                 "RELLENO", "CAPITULO", "INTERNO", "TIEMPO", "PADRES", "FUGAS", "TEMPLO",
                 "GUSANO", "HECHIZO", "ESPINA", "ATLETA", "MENTIRA", "REVISTA", "RECIBO", "RESPALDO"]

    selectWords = []

    # palabra horizontal
    elem = random.randrange(len(wordsList))
    word = wordsList.pop(elem)
    row = random.randrange(numRows)
    col = random.randrange(numColumns - len(word))
    i = col
    while i - col != len(word):
        matrix[row][i] = word[i - col]
        i += 1

    selectWords += [word]

    # palabra vertical
    verticalValues = verticalWord(matrix, wordsList, numRows, numColumns)
    matrix = verticalValues[0]
    wordsList = verticalValues[1]
    selectWords += [verticalValues[2]]

    #palabra diagonal izquierda negativa
    diagonalValues = diagonalLeftNegativeWord(matrix, wordsList, numRows, numColumns)
    matrix = diagonalValues[0]
    wordsList = diagonalValues[1]
    selectWords += [diagonalValues[2]]
    
    #palabra diagonal izquierda positiva
    diagonalValues2 = diagonalLeftPositiveWord(matrix, wordsList, numRows, numColumns)
    matrix = diagonalValues2[0]
    wordsList = diagonalValues2[1]
    selectWords += [diagonalValues2[2]]

    print()
    printMatrix(matrix)
    return [matrix, selectWords]


def verticalWord(matrix, wordsList, numRows, numColumns):

    matrixCopy = [x[:] for x in matrix]
    wordsListCopy = list(wordsList) 

    elem = random.randrange(len(wordsList))
    word = wordsListCopy.pop(elem)
    row = random.randrange(numRows - len(word))
    col = random.randrange(numColumns)
    i = row
    
    while i - row != len(word):
        if matrixCopy[i][col] == 0:
            matrixCopy[i][col] = word[i - row]
            i += 1
        elif matrixCopy[i][col] == word[i - row]:
            matrixCopy[i][col] = word[i - row]
            i += 1
        else:
            return verticalWord(matrix, wordsList, numRows, numColumns)

    return [matrixCopy, wordsListCopy, word]


def diagonalLeftNegativeWord(matrix, wordsList, numRows, numColumns):

    matrixCopy = [x[:] for x in matrix]
    wordsListCopy = list(wordsList) 

    elem = random.randrange(len(wordsList))
    word = wordsListCopy.pop(elem)
    row = random.randrange(numRows + 1 - len(word))
    col = random.randrange(numColumns + 1 - len(word))
    i = row
    
    while i - row != len(word):
        if matrixCopy[i][i] == 0:
            matrixCopy[i][i] = word[i - row]
            i += 1
        elif matrixCopy[i][i] == word[i - row]:
            matrixCopy[i][i] = word[i - row]
            i += 1
        else:
            return diagonalLeftNegativeWord(matrix, wordsList, numRows, numColumns)

    return [matrixCopy, wordsListCopy, word]


def diagonalLeftPositiveWord(matrix, wordsList, numRows, numColumns):

    matrixCopy = [x[:] for x in matrix]
    wordsListCopy = list(wordsList) 

    elem = random.randrange(len(wordsList))
    word = wordsListCopy.pop(elem)
    row = random.randrange(numRows + 1 - len(word), numRows)
    col = random.randrange(numColumns + 1 - len(word))
    count = 0
    
    while count != len(word):
        if matrixCopy[row][col] == 0:
            matrixCopy[row][col] = word[count]
            count += 1
            row -= 1
            col +=1
        elif matrixCopy[row][col] == word[count]:
            matrixCopy[row][col] = word[count]
            count += 1
            row -= 1
            col += 1
        else:
            return diagonalLeftPositiveWord(matrix, wordsList, numRows, numColumns)

    return [matrixCopy, wordsListCopy, word]


def fillBoardSopa(matrix):

    numRows = len(matrix)
    numColumns = len(matrix[0])

    matrixCopy = [x[:] for x in matrix]

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(letters)
    
    for row in range(numRows):
        for col in range(numColumns):
            if matrixCopy[row][col] == 0:
                elem = random.randrange(length)
                matrixCopy[row][col] = letters[elem]

    return matrixCopy


def fillSpacePlayerSopa(upperMatrix, row, col):

    if upperMatrix[row][col] == 0:
        upperMatrix[row][col] = 1
        return True
    else:
        return False


def checkWord(lowerMatrix, wordPos):

    if wordPos == []:
        return False

    for pos in wordPos:
        row = pos[0]
        col = pos[1]
        if lowerMatrix[row][col] == 0:
            return False

    return True


def checkWinnerSopa(lowerMatrix, upperMatrix):

    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])
    
    for row in range(numRows):
        for col in range(numColumns):
            if lowerMatrix[row][col] == 0 and upperMatrix[row][col] != 0:
                return False
            elif lowerMatrix[row][col] != 0 and upperMatrix[row][col] == 0:
                return False

    return True



def changeSpaceNum(upperMatrix):

    numRows = len(upperMatrix)
    numColumns = len(upperMatrix[0])
    
    for row in range(numRows):
        for col in range(numColumns):
            if upperMatrix[row][col] == 1:
                upperMatrix[row][col] = 2

    return




def startGameSopa(player, playersCompleteInfo):

    gameMode = random.randrange(3)

    if gameMode == 0:
        board = createBoardSopa(formMatrix(10,10))
        return gameSopa(board[0], formMatrix(10,10), board[1], 75, player, playersCompleteInfo)

    elif gameMode == 1:
        board = createBoardSopa(formMatrix(15,15))
        return gameSopa(board[0], formMatrix(15,15), board[1], 60, player, playersCompleteInfo)

    else:
        board = createBoardSopa(formMatrix(20,20))
        return gameSopa(board[0], formMatrix(20,20), board[1], 45, player, playersCompleteInfo)


def gameSopa(lowerMatrix, upperMatrix, wordsList, SQUARESIZE, player, playersCompleteInfo):

    gameOver = False

    widthDisplay = 1300
    heightDisplay = 920
    
    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])

    sopaDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    
    backgroundImage = pygame.image.load("old_paper_texture.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    filledLowerMatrix = fillBoardSopa(lowerMatrix)

    upperMatrixCopy = [x[:] for x in upperMatrix]

    sopaDisplay.blit(backgroundImage, (0,0))
    drawBoardSopa(filledLowerMatrix, upperMatrixCopy, sopaDisplay, SQUARESIZE)
    pygame.display.update()

    wordsFound = 0

    wordPos = []

    seconds = 0

    iniTime = time.time()
    timer = 0
    maxTime = 120            #Tiempo maximo para el juego en segundos
    while timer < maxTime:
        endTime = time.time()
        timer = endTime - iniTime
        #Ejemplo cuenta regresiva
#        print(int(maxTime-timer))
        
        timeLeft = myFont.render(("Seconds left: " + str(int(maxTime - timer))), True, (69,69,69))
        checkIcon = myFont.render(("Check Word!!!"), True, (69,69,69))
        
        sopaDisplay.blit(backgroundImage, (0,0))
        sopaDisplay.blit(timeLeft, (940, 750))
        sopaDisplay.blit(checkIcon, (960, 600))
        drawBoardSopa(filledLowerMatrix, upperMatrix, sopaDisplay, SQUARESIZE)

        for i in range(1, 5):
            showWord = wordsList[i - 1]
            showWord = myFont.render((showWord), True, (69,69,69))
            sopaDisplay.blit(showWord, (960, 60 * i))
                   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if inArea(0,0, SQUARESIZE * numRows, SQUARESIZE * numColumns, sopaDisplay):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    posx = event.pos[0]
                    posy = event.pos[1]
                    
                    row = int(math.floor(posy/ SQUARESIZE))
                    column = int(math.floor(posx/ SQUARESIZE))
                    if fillSpacePlayerSopa(upperMatrix, row, column):
                        drawBoardSopa(filledLowerMatrix, upperMatrix, sopaDisplay, SQUARESIZE)
                        pygame.display.update()
                        wordPos += [[row, column]]


        if buttonInGame(960, 600, 250, 45, sopaDisplay, 250, 5):
            if checkWord(lowerMatrix, wordPos):
                changeSpaceNum(upperMatrix)
                upperMatrixCopy = [x[:] for x in upperMatrix]
                wordPos = []
                wordsFound += 1
                
            if checkWinnerSopa(lowerMatrix, upperMatrix):
                changeSpaceNum(upperMatrix)
                upperMatrixCopy = [x[:] for x in upperMatrix]
                wordsFound = 4
            else:
                upperMatrix = [x[:] for x in upperMatrixCopy]
                wordPos = []
                
            drawBoardSopa(filledLowerMatrix, upperMatrix, sopaDisplay, SQUARESIZE)
            pygame.display.update()


        if wordsFound == 4:
            timer = 250

##        pygame.time.wait(1000)
##        seconds += 1
##        print(seconds)
##        if seconds == 20:
##            gameOver = True

    pygame.time.wait(3500) 
    if wordsFound == 4:
        return winnerScreen(player, playersCompleteInfo, True)
        
    else:
        return winnerScreen(player, playersCompleteInfo, False)
    
            
def drawBoardSopa(lowerMatrix, upperMatrix, screen, SQUARESIZE):

    global BLUE, GRAY, RED, YELLOW, WHITE, myFont, LIGHTGREEN
    numRows = len(lowerMatrix)
    numColumns = len(lowerMatrix[0])
    
    RADIUS = int(SQUARESIZE/2 - 5)
    
    for r in range(numRows):
        for c in range(numColumns):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            letter = lowerMatrix[r][c]
            if numRows == 10:
                letter = myFont.render((letter), True, (69,69,69))
            elif numRows == 15:
                letter = myFontSmall.render((letter), True, (69,69,69))
            elif numRows == 20:
                letter = myFontSmaller.render((letter), True, (69,69,69))
            screen.blit(letter, (int(c*SQUARESIZE+SQUARESIZE/3), int(r*SQUARESIZE+SQUARESIZE/6)))
    
    for r in range(numRows):
        for c in range(numColumns):		
            if upperMatrix[r][c] != 0:
                
                if upperMatrix[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                if upperMatrix[r][c] == 2:
                    pygame.draw.circle(screen, LIGHTGREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                    
                letter = lowerMatrix[r][c]
                if numRows == 10:
                    letter = myFont.render((letter), True, (69,69,69))
                elif numRows == 15:
                    letter = myFontSmall.render((letter), True, (69,69,69))
                elif numRows == 20:
                    letter = myFontSmaller.render((letter), True, (69,69,69))
                screen.blit(letter, (int(c*SQUARESIZE+SQUARESIZE/3), int(r*SQUARESIZE+SQUARESIZE/6)))

    pygame.display.update()
            


###########################################################################################################################################################
###################################################################### CHOOSE ORDER #######################################################################

def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])




    


def menuPrincipal():
    
    global myFont
    
    widthDisplay = 1300
    heightDisplay = 800

    menuPrincipalDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()

    backgroundImage = pygame.image.load("menuPrincipal3.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    startGameText = myFont.render(("START GAME"), True, (255,255,255))


    inMenu = True

    while inMenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        menuPrincipalDisplay.blit(backgroundImage, (0,0))
        menuPrincipalDisplay.blit(startGameText, ((widthDisplay//2) - (widthDisplay//12), 250))

        if buttonInGame(((widthDisplay//2) - (widthDisplay//12)), 250, 240, 50, menuPrincipalDisplay, 240, -3):
            startInfo = menuSelNumOfPlayers()
            playersList = startInfo[0]
            playersCompleteInfo = startInfo[1]
            return mainMap(playersList, playersCompleteInfo)

        pygame.display.update()
        
        clock.tick(60)


def menuSelNumOfPlayers():

    global myFont, myFontLarge, luffyPiece, zoroPiece, sanjiPiece, namiPiece
    
    widthDisplay = 1300
    heightDisplay = 800

    numPlayersDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()

    backgroundImage = pygame.image.load("black_background.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    numOfPlayerMsg = myFontLarge.render(("SELECT NUMBER OF PLAYERS"), True, (255,255,255))

    twoPlayers = myFont.render(("TWO PLAYERS"), True, (255,255,255))
    threePlayers = myFont.render(("THREE PLAYERS"), True, (255,255,255))
    fourPlayers = myFont.render(("FOUR PLAYERS"), True, (255,255,255))
    
    inMenu = True

    while inMenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        
        numPlayersDisplay.blit(backgroundImage, (0,0))
        numPlayersDisplay.blit(numOfPlayerMsg, (widthDisplay//4, 75))
        numPlayersDisplay.blit(twoPlayers, (widthDisplay//8, 300))
        numPlayersDisplay.blit(threePlayers, (widthDisplay//8, 400))
        numPlayersDisplay.blit(fourPlayers, (widthDisplay//8, 500))

        #twoPlayers button
        if inArea(widthDisplay//8, 300, 260, 50, numPlayersDisplay):
            numPlayersDisplay.blit(zoroPiece, (750,300))
            numPlayersDisplay.blit(luffyPiece, (600,300))
            if buttonInGame(widthDisplay//8, 300, 260, 50, numPlayersDisplay, 250, -3):
                playersList = playerEnter(2)
                showNewOrder(playersList)
                return selectCharacter(playersList)

        #threPlayers button
        if inArea(widthDisplay//8, 400, 285, 50, numPlayersDisplay):
            numPlayersDisplay.blit(zoroPiece, (850,300))
            numPlayersDisplay.blit(sanjiPiece, (425,300))
            numPlayersDisplay.blit(luffyPiece, (700,300))
            if buttonInGame(widthDisplay//8, 400, 285, 50, numPlayersDisplay, 275, -3):
                playersList = playerEnter(3)
                showNewOrder(playersList)
                return selectCharacter(playersList)
        #fourPlayers button
        if inArea(widthDisplay//8, 500, 275, 50, numPlayersDisplay):
            numPlayersDisplay.blit(zoroPiece, (900,300))
            numPlayersDisplay.blit(namiPiece, (320,300))
            numPlayersDisplay.blit(sanjiPiece, (475,300))                        
            numPlayersDisplay.blit(luffyPiece, (750,300))            
            if buttonInGame(widthDisplay//8, 500, 275, 50, numPlayersDisplay, 265, -3):
                playersList = playerEnter(4)
                showNewOrder(playersList)
                return selectCharacter(playersList)
            
        pygame.display.update()
        
        clock.tick(60)


def playersNameMenu(numOfPlayers):

    global myFont, WHITE
    
    widthDisplay = 800
    heightDisplay = 600

    gameDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("insert_names.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    nameList = []
    playerNum = 1
    
    inMenu = True
      
    while numOfPlayers > 0:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                inMenu = False
        
        gameDisplay.blit(backgroundImage, (0,0))

       
        playerName = ask(gameDisplay, ("Enter name - Player " + str(playerNum)), 65, heightDisplay//3, WHITE)
        nameList += [[playerName]]
        numOfPlayers -= 1
        playerNum += 1
        
        pygame.display.update()

    return nameList


def playersNumberMenu(nameList):

    global myFont, WHITE
    
    widthDisplay = 800
    heightDisplay = 600

    gameDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("insert_names.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    numOfPlayers = len(nameList)
    
    selectNumList = []
    playerNum = 0
    
    inMenu = True
      
    while numOfPlayers > 0:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                inMenu = False
        
        gameDisplay.blit(backgroundImage, (0,0))
       
        selectNum = ask(gameDisplay, ("Enter Number (1 - 1000) " + nameList[playerNum][0]), 65, heightDisplay//3, WHITE)
        try:
            selectNum = int(selectNum)
            if selectNum > 1000:
                return playersNumberMenu(nameList)
        except:
            return playersNumberMenu(nameList)
            
        nameList[playerNum] += [selectNum]
        numOfPlayers -= 1
        playerNum += 1
        
        pygame.display.update()

    return nameList


def selectOrderMap(nameList):

    newNameList = []
    numList = []

    for i in nameList:
        numList += [i[1]]

    selectList = selectOrder(numList)   
    numList = selectList[0]
    randomNum = selectList[1]
    print(randomNum)

    for i in numList:
        for j in nameList:
            if j[0] not in newNameList:
                if abs(randomNum - j[1]) == i:
                    newNameList += [j[0]]
                
    return newNameList

            


def selectOrder(selectNumList):

    randomNum = random.randrange(1001)
    newList = []
    
    for i in selectNumList:
        newList += [abs(randomNum - i)]

    newList = qsort(newList)

    return [newList, randomNum]

def playerEnter(numOfPlayers):

    nameList = playersNameMenu(numOfPlayers)
    nameNumList = playersNumberMenu(nameList)
    newOrderNameList = selectOrderMap(nameNumList)

    return newOrderNameList


def showNewOrder(playersList):

    global myFont, myFontLarge, WHITE
    
    widthDisplay = 800
    heightDisplay = 800

    showNewOrderDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("insert_names.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))
    showNewOrderDisplay.blit(backgroundImage, (0,0))

    newOrderMsg = myFontLarge.render(("NEW ORDER"), True, (255,255,255))
    showNewOrderDisplay.blit(newOrderMsg, (widthDisplay//3, 25))

    numOfPlayers = len(playersList)

    for player in range(numOfPlayers):
        playerMsg = myFont.render(("PLAYER " + str(player + 1) + ": " + str(playersList[player])), True, (WHITE))
        showNewOrderDisplay.blit(playerMsg, (widthDisplay//3, ((player + 1) * 100) + 25))        
    
              
    pygame.display.update()
    pygame.time.wait(7000)
    return


    
###########################################################################################################################################################
################################################################# PLAYERS PIECE ###########################################################################

frankyPiece = pygame.image.load("franky_piece.png")
frankyPiece = pygame.transform.scale(frankyPiece, (700,700))

usoppPiece = pygame.image.load("usopp_piece2.png")
usoppPiece = pygame.transform.scale(usoppPiece, (400,700))

namiPiece = pygame.image.load("nami_piece2.png")
namiPiece = pygame.transform.scale(namiPiece, (700,700))

zoroPiece = pygame.image.load("zoro_piece2.png")
zoroPiece = pygame.transform.scale(zoroPiece, (400,700))

luffyPiece = pygame.image.load("luffy_piece2.png")
luffyPiece = pygame.transform.scale(luffyPiece, (400,700))

sanjiPiece = pygame.image.load("sanji_piece2.png")
sanjiPiece = pygame.transform.scale(sanjiPiece, (700,700))

robinPiece = pygame.image.load("robin_piece.png")
robinPiece = pygame.transform.scale(robinPiece, (400,700))

chopperPiece = pygame.image.load("chopper_piece2.png")
chopperPiece = pygame.transform.scale(chopperPiece, (900,700))

brookPiece = pygame.image.load("brook_piece.png")
brookPiece = pygame.transform.scale(brookPiece, (700,700))

jinbePiece = pygame.image.load("jinbe_piece.png")
jinbePiece = pygame.transform.scale(jinbePiece, (700,700))

###########################################################################################################################################################
################################################################# PLAYERS ICON ############################################################################

frankyIcon =  pygame.image.load("ficha_Franky.png")
frankyIcon = pygame.transform.scale(frankyIcon, (85,110))

usoppIcon = pygame.image.load("ficha_Usopp.png")
usoppIcon = pygame.transform.scale(usoppIcon, (85,110))

namiIcon = pygame.image.load("ficha_Nami.png")
namiIcon = pygame.transform.scale(namiIcon, (85,110))

zoroIcon = pygame.image.load("ficha_Zoro.png")
zoroIcon = pygame.transform.scale(zoroIcon, (85,110))

luffyIcon = pygame.image.load("ficha_Luffy.png")
luffyIcon = pygame.transform.scale(luffyIcon, (85,110))

sanjiIcon = pygame.image.load("ficha_Sanji.png")
sanjiIcon = pygame.transform.scale(sanjiIcon, (85,110))

robinIcon = pygame.image.load("ficha_Robin.png")
robinIcon = pygame.transform.scale(robinIcon, (85,110))

chopperIcon = pygame.image.load("ficha_Chopper.png")
chopperIcon = pygame.transform.scale(chopperIcon, (85,110))

brookIcon = pygame.image.load("ficha_Brook.png")
brookIcon = pygame.transform.scale(brookIcon, (85,110))

jinbeIcon = pygame.image.load("ficha_Jinbe.png")
jinbeIcon = pygame.transform.scale(jinbeIcon, (85,110))

###########################################################################################################################################################
############################################################### SELECT CHARACTER MENU #####################################################################

def selectCharacter(playersList):

    global myFont, myFontSmall, myFontLarge, frankyIcon, frankyPiece, usoppIcon, usoppPiece, namiIcon, namiPiece, zoroIcon, zoroPiece, luffyIcon, luffyPiece, sanjiIcon, sanjiPiece, robinIcon, robinPiece, chopperIcon, chopperPiece, brookIcon, brookPiece, jinbeIcon, jinbePiece
    
    widthDisplay = 1300
    heightDisplay = 800

    selectCharDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()

    backgroundImage = pygame.image.load("select_character.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    playersCompleteInfo = {}

    characterPack = []

    numOfPlayers = len(playersList)
    playerNum = 0
                                        
    while numOfPlayers > 0:

        selectTurnMsg = myFontLarge.render(("SELECT YOUR CHARACTER " + str(playersList[playerNum])), True, (255,255,255))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                            
        selectCharDisplay.blit(backgroundImage, (0,0))
        selectCharDisplay.blit(selectTurnMsg, (widthDisplay//5, 50))

        # select franky        
        if inArea(40, 340, 200, 280, selectCharDisplay):
            selectCharDisplay.blit(frankyIcon, (105, 225))
            
            if frankyPiece not in characterPack:
                charMsg = myFontSmall.render(("FRANKY"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (100, 190))
                
                if buttonInGameVer2(40, 340, 200, 280, selectCharDisplay):
                    characterPack += [frankyPiece]
                    newKey = {playersList[playerNum] : [frankyIcon, frankyPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)

                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("FRANKY - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (50, 190))

        # select usopp        
        if inArea(247, 420, 88, 200, selectCharDisplay):
            selectCharDisplay.blit(usoppIcon, (257, 310))
            
            if usoppPiece not in characterPack:
                charMsg = myFontSmall.render(("USOPP"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (257, 275))
                
                if buttonInGameVer2(247, 420, 88, 200, selectCharDisplay):
                    characterPack += [usoppPiece]
                    newKey = {playersList[playerNum] : [usoppIcon, usoppPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("USOPP - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (217, 275))

        # select nami        
        if inArea(345, 420, 70, 200, selectCharDisplay):
            selectCharDisplay.blit(namiIcon, (330, 315))
            
            if namiPiece not in characterPack:
                charMsg = myFontSmall.render(("NAMI"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (335, 280))
                
                if buttonInGameVer2(345, 420, 70, 200, selectCharDisplay):
                    characterPack += [namiPiece]
                    newKey = {playersList[playerNum] : [namiIcon, namiPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("NAMI - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (290, 280))

        # select zoro        
        if inArea(417, 417, 106, 203, selectCharDisplay):
            selectCharDisplay.blit(zoroIcon, (426, 305))
            
            if zoroPiece not in characterPack:
                charMsg = myFontSmall.render(("ZORO"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (432, 270))
                
                if buttonInGameVer2(417, 417, 106, 203, selectCharDisplay):
                    characterPack += [zoroPiece]
                    newKey = {playersList[playerNum] : [zoroIcon, zoroPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("ZORO - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (395, 270))

        # select luffy        
        if inArea(525, 420, 78, 200, selectCharDisplay):
            selectCharDisplay.blit(luffyIcon, (517, 310))
            
            if luffyPiece not in characterPack:
                charMsg = myFontSmall.render(("LUFFY"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (520, 275))
                
                if buttonInGameVer2(525, 420, 78, 200, selectCharDisplay):
                    characterPack += [luffyPiece]
                    newKey = {playersList[playerNum] : [luffyIcon, luffyPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("LUFFY - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (485, 275))
                
        # select sanji        
        if inArea(605, 414, 115, 206, selectCharDisplay):
            selectCharDisplay.blit(sanjiIcon, (608, 300))

            if sanjiPiece not in characterPack:
                charMsg = myFontSmall.render(("SANJI"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (612, 265))
                
                if buttonInGameVer2(605, 414, 115, 206, selectCharDisplay):
                    characterPack += [sanjiPiece]
                    newKey = {playersList[playerNum] : [sanjiIcon, sanjiPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("SANJI - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (575, 265))

        # select robin        
        if inArea(726, 405, 75, 215, selectCharDisplay):
            selectCharDisplay.blit(robinIcon, (718, 290))
            
            if robinPiece not in characterPack:
                charMsg = myFontSmall.render(("ROBIN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (721, 255))
                
                if buttonInGameVer2(726, 405, 75, 215, selectCharDisplay):
                    characterPack += [robinPiece]
                    newKey = {playersList[playerNum] : [robinIcon, robinPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("ROBIN - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (685, 255))

        # select chopper        
        if inArea(803, 530, 99, 90, selectCharDisplay):
            selectCharDisplay.blit(chopperIcon, (808, 415))
            
            if chopperPiece not in characterPack:
                charMsg = myFontSmall.render(("CHOPPER"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (800, 380))
                
                if buttonInGameVer2(803, 530, 99, 90, selectCharDisplay):
                    characterPack += [chopperPiece]
                    newKey = {playersList[playerNum] : [chopperIcon, chopperPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("CHOPPER - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (760, 380))

        # select brook        
        if inArea(906, 505, 79, 115, selectCharDisplay) or inArea(870, 260, 155, 246, selectCharDisplay):
            selectCharDisplay.blit(brookIcon, (903, 175))
            
            if brookPiece not in characterPack:
                charMsg = myFontSmall.render(("BROOK"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (906, 140))
                
                if buttonInGameVer2(906, 505, 79, 115, selectCharDisplay) or buttonInGameVer2(870, 260, 155, 246, selectCharDisplay):
                    characterPack += [brookPiece]
                    newKey = {playersList[playerNum] : [brookIcon, brookPiece, 0, 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("BROOK - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (870, 140))
                    
        # select jinbe        
        if inArea(1027, 260, 245, 360, selectCharDisplay):
            selectCharDisplay.blit(jinbeIcon, (1108, 155))
            
            if jinbePiece not in characterPack:
                charMsg = myFontSmall.render(("JINBE"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (1110, 120))
                
                if buttonInGameVer2(1027, 260, 245, 360, selectCharDisplay):
                    characterPack += [jinbePiece]
                    newKey = {playersList[playerNum] : [jinbeIcon, jinbePiece, 0 , 0]}
                    playersCompleteInfo.update(newKey)
                    playerNum += 1
                    numOfPlayers -= 1
            else:
                charMsg = myFontSmall.render(("JINBE - TAKEN"), True, (255,255,255))
                selectCharDisplay.blit(charMsg, (1075, 120))
                    

        pygame.display.update()

    pygame.display.update()
    return [playersList, playersCompleteInfo]


###########################################################################################################################################################
############################################################### SELECT CHARACTER MENU #####################################################################

diceIcon = pygame.image.load("dados.png")
diceIcon = pygame.transform.scale(diceIcon, (220,175))

diceShadowIcon = pygame.image.load("dados_sombra.png")
diceShadowIcon = pygame.transform.scale(diceShadowIcon, (220,175))


def mainMap(playersList, playersCompleteInfo):

    global myFont, myFontSmall, myFontLarge, diceIcon, diceShadowIcon, BLACK
    
    widthDisplay = 1600
    heightDisplay = 950

    mapBoardDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()

##    mapFunctions = { "game1" : startGameTicTacToe, "game2" : startGameTicTacToe, "game3" : startGameSopa, "game4" : startGameSopa,
##                                   "game5" : startGameMemory, "game6" : startGameMemory, "game7" : startGameGsWho, "game8" : startGameGsWho,
##                                   "game9" : startGameGsThePath, "game10" : startGameGsThePath, "game11" : startGameFlipCards, "game12" : startGameFlipCards,
##                                   "game13" : startGameColTheTrea, "game14" : startGameColTheTrea, "game15" : startGameCat, "game16" : startGameCat,
##                                   "game17" : startGameBomber, "game18" : startGameBomber}
##    
##    mapFunctionsKey = ['game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9', 'game10', 'game11', 'game12', 'game13', 'game14', 'game15', 'game16', 'game17', 'game18']

    mapFunctions = [startGameTicTacToe, startGameTicTacToe, startGameSopa, startGameSopa,
                                   startGameMemory, startGameMemory, startGameGsWho, startGameGsWho,
                                   startGameGsThePath, startGameGsThePath, startGameFlipCards, startGameFlipCards,
                                   startGameColTheTrea, startGameColTheTrea, startGameCat, startGameCat,
                                   startGameBomber, startGameBomber, "tube1", "tube2", "tube3", "carcel", "estrella", "fuego", "hielo", "cola"]
    random.shuffle(mapFunctions)
    mapFunctions = ["offset"] + mapFunctions
    
    mapPlayers = [list(playersList), [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    backgroundImage = pygame.image.load("mapa_tablero.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    numOfPlayers = len(playersList)
    playerTurn = 0
    
    print(playersCompleteInfo)
    print(playersList)
    print(mapPlayers)

    drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
    
    while mapPlayers[27] == []:

        if playerTurn == numOfPlayers:
            playerTurn = 0
            
        rollDiceMsg = myFontLarge.render(("ROLL THE DICE " + str(playersList[playerTurn])), True, (BLACK))

        # revisar si pierde turno
        if playersCompleteInfo[playersList[playerTurn]][2] > 0:
            mapBoardDisplay.blit(backgroundImage, (0,0))
            rollDiceMsg = myFontLarge.render(("WAIT FOR YOUR TURN:" + str(playersList[playerTurn])), True, (BLACK))
            mapBoardDisplay.blit(rollDiceMsg, (760,777))
            drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
            pygame.time.wait(2000)
            playersCompleteInfo[playersList[playerTurn]][2] -= 1
            playerTurn += 1
                
        mapBoardDisplay.blit(backgroundImage, (0,0))
        mapBoardDisplay.blit(rollDiceMsg, (760,777))
        mapBoardDisplay.blit(diceIcon, (810,655))
        drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if inArea(810, 655, 220, 175, mapBoardDisplay):
            mapBoardDisplay.blit(backgroundImage, (0,0))            
            mapBoardDisplay.blit(rollDiceMsg, (760,777))
            mapBoardDisplay.blit(diceShadowIcon, (810,655))
            drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
            if buttonInGameVer2(810, 655, 220, 175, mapBoardDisplay):
                movePos = random.randrange(1,7)
                playerName = playersList[playerTurn]
                currentPos = playersCompleteInfo[playerName][3]

                if movePos <= 4:
                    if currentPos + movePos >= 27:    #se llego al final
                        mapPlayers[currentPos].remove(playerName)
                        mapPlayers[27] += [playerName]
                        mapBoardDisplay.blit(backgroundImage, (0,0))
                        rollDiceMsg = myFontLarge.render((str(playerName) + " MOVES " + str(movePos) + " SPACES"), True, (BLACK))
                        mapBoardDisplay.blit(rollDiceMsg, (760,777))
                        drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
                        pygame.time.wait(2000)
                    else:
                        mapBoardDisplay.blit(backgroundImage, (0,0))
                        rollDiceMsg = myFontLarge.render((str(playerName) + " MOVES " + str(movePos) + " SPACES"), True, (BLACK))
                        mapBoardDisplay.blit(rollDiceMsg, (760,777))
                        drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
                        pygame.time.wait(2000)                        
                        playerTurn = rollTheDice(playersList, playersCompleteInfo, playerTurn, mapFunctions, mapPlayers, widthDisplay, backgroundImage, movePos, mapBoardDisplay)
                            
                if movePos > 4:
                    mapBoardDisplay.blit(backgroundImage, (0,0))
                    rollDiceMsg = myFontLarge.render(("LOSES TURN: " + str(playerName)), True, (BLACK))
                    mapBoardDisplay.blit(rollDiceMsg, (760,777))
                    drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
                    pygame.time.wait(2000)
                    playerTurn += 1

                print(playersList)
                print(playersCompleteInfo)
                print(playerTurn)
                print(mapFunctions)
                print(mapPlayers)

                mapBoardDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
            
                                   
        pygame.display.update()

    ultimateWinner = mapPlayers[27][0]
    return finalWinnerScreen(ultimateWinner)



###########################################################################################################################################################
#################################################################### SPECIAL ICONS ########################################################################

carcelIcon = pygame.image.load("carcel.png")
carcelIcon = pygame.transform.scale(carcelIcon, (90,95))

estrellaIcon = pygame.image.load("estrella.png")
estrellaIcon = pygame.transform.scale(estrellaIcon, (90,95))

tubeIcon = pygame.image.load("pozo.png")
tubeIcon = pygame.transform.scale(tubeIcon, (90,95))

fireIcon = pygame.image.load("fruta_fuego.png")
fireIcon = pygame.transform.scale(fireIcon, (90,95))

iceIcon = pygame.image.load("fruta_hielo.png")
iceIcon = pygame.transform.scale(iceIcon, (90,95))

barcoIcon = pygame.image.load("barco_volando.png")
barcoIcon = pygame.transform.scale(barcoIcon, (90,95))


specialIcons = {"carcel" : carcelIcon, "estrella" : estrellaIcon, "tube1" : tubeIcon, "tube2" : tubeIcon, "tube3" : tubeIcon, "fuego" : fireIcon, "hielo" : iceIcon, "cola" : barcoIcon}


def drawBoardMap(mapPlayers, playersCompleteInfo, screen, mapFunctions):

    global specialIcons

    posList = [(150,700), (110,530), (150,330), (148,180),
               (270,110), (395,180), (340,325), (400,445),
               (385,585), (460,740), (640,735), (650,560),
               (610,430), (625,275), (720,155), (860,120),
               (925,245), (890,380), (980,500), (1090,400),
               (1150,265), (1260,135), (1325,283), (1265,415),
               (1180,555), (1200,717), (1350,645), (1475,510)]

    widthIcon = 85//2
    heightIcon = 110

    numOfBoxes = len(mapPlayers)

    for box in range(numOfBoxes):

        offset = box + 1
        if offset < numOfBoxes - 1:
            function = mapFunctions[offset]
            if type(function) == str:
                xPos = posList[offset][0] - 17
                yPos = posList[offset][1] - 17
                showFunction = specialIcons[function]
                screen.blit(showFunction, (xPos, yPos))


        numPieces = len(mapPlayers[box])
        selectInBox = mapPlayers[box]
        xPos = posList[box][0] - widthIcon
        yPos = posList[box][1] - heightIcon

        for piece in range(numPieces):
            if piece == 0:
                showPiece = playersCompleteInfo[selectInBox[piece]][0]
                screen.blit(showPiece, (xPos, yPos))
            if piece == 1:
                showPiece = playersCompleteInfo[selectInBox[piece]][0]
                screen.blit(showPiece, (xPos + 50, yPos))
            if piece == 2:
                showPiece = playersCompleteInfo[selectInBox[piece]][0]
                screen.blit(showPiece, (xPos, yPos + 60))                
            if piece == 3:
                showPiece = playersCompleteInfo[selectInBox[piece]][0]
                screen.blit(showPiece, (xPos + 50 , yPos + 60))

    pygame.display.update()




def rollTheDice(playersList, playersCompleteInfo, playerTurn, mapFunctions, mapPlayers, widthDisplay, backgroundImage, movePos, mapBoardDisplay):

    print(playersList)
    print(playersCompleteInfo)
    print(playerTurn)
    print(mapFunctions)
    print(mapPlayers)

    playerName = playersList[playerTurn]
    originalPos = playersCompleteInfo[playerName][3]
    mapPlayers[originalPos].remove(playerName)
        
    playersCompleteInfo[playerName][3] += movePos
    currentPos = playersCompleteInfo[playerName][3]
    mapPlayers[currentPos] += [playerName]
    mapBoardDisplay.blit(backgroundImage, (0,0))
    drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
    pygame.time.wait(2000)

    try:
        # funciones de tubo
        if mapFunctions[currentPos] == "tube1":
            tubeIndex = mapFunctions.index("tube2")
            mapPlayers[currentPos].remove(playerName)
            playersCompleteInfo[playerName][3] = tubeIndex                        
            mapPlayers[tubeIndex] += [playerName]
            playerTurn += 1
            return playerTurn
            
        elif mapFunctions[currentPos] == "tube2":
            tubeIndex = mapFunctions.index("tube3")
            mapPlayers[currentPos].remove(playerName)
            playersCompleteInfo[playerName][3] = tubeIndex
            mapPlayers[tubeIndex] += [playerName]
            playerTurn += 1
            return playerTurn

        elif mapFunctions[currentPos] == "tube3":
            tubeIndex = mapFunctions.index("tube1")
            mapPlayers[currentPos].remove(playerName)
            playersCompleteInfo[playerName][3] = tubeIndex
            mapPlayers[tubeIndex] += [playerName]
            playerTurn += 1
            return playerTurn

        elif mapFunctions[currentPos] == "carcel":
            playersCompleteInfo[playersList[playerTurn]][2] += 2
            playerTurn += 1
            return playerTurn

        elif mapFunctions[currentPos] == "estrella":
            rollDiceMsg = myFontLarge.render(("ROLL THE DICE AGAIN " + str(playerName)), True, (0,0,0))                    
            mapBoardDisplay.blit(backgroundImage, (0,0))
            mapBoardDisplay.blit(rollDiceMsg, (760,777))
            drawBoardMap(mapPlayers, playersCompleteInfo, mapBoardDisplay, mapFunctions)
            pygame.time.wait(1000)
            return playerTurn

        elif mapFunctions[currentPos] == "fuego":
            firePower(playersList, playersCompleteInfo, mapPlayers)
            playerTurn += 1
            return playerTurn

        elif mapFunctions[currentPos] == "hielo":
            icePower(playersList, playersCompleteInfo)
            playerTurn += 1
            return playerTurn

        elif mapFunctions[currentPos] == "cola":
            jumpPos = random.randrange(1,4)
            return rollTheDice(playersList, playersCompleteInfo, playerTurn, mapFunctions, mapPlayers, widthDisplay, backgroundImage, jumpPos, mapBoardDisplay)        
                                        
        else:                
            if mapFunctions[currentPos] == startGameTicTacToe or mapFunctions[currentPos] == startGameMemory:
                playersListCopy = list(playersList)
                playersListCopy.remove(playerName)
                secondPlayer = random.randrange(len(playersListCopy))
                secondPlayer = playersListCopy[secondPlayer]
                versusScreen(2, [playerName, secondPlayer])
                if mapFunctions[currentPos]([playerName, secondPlayer], playersCompleteInfo):
                    playerTurn += 1
                    return playerTurn
                else:
                    mapPlayers[currentPos].remove(playerName)
                    mapPlayers[originalPos] += [playerName]
                    playersCompleteInfo[playerName][3] = originalPos
                    playerTurn += 1
                    return playerTurn

            elif mapFunctions[currentPos] == startGameFlipCards:
                versusScreen(4, [])
                if mapFunctions[currentPos](playerName, playersList, playersCompleteInfo):
                    playerTurn += 1
                    return playerTurn
                else:
                    mapPlayers[currentPos].remove(playerName)
                    mapPlayers[originalPos] += [playerName]
                    playersCompleteInfo[playerName][3] = originalPos
                    playerTurn += 1
                    return playerTurn

            else:
                versusScreen(1, [playerName])
                if mapFunctions[currentPos](playerName, playersCompleteInfo):
                    playerTurn += 1
                    return playerTurn
                else:
                    mapPlayers[currentPos].remove(playerName)
                    mapPlayers[originalPos] += [playerName]
                    playersCompleteInfo[playerName][3] = originalPos
                    playerTurn += 1
                    return playerTurn
    except:
        playerTurn += 1
        return playerTurn


def versusScreen(gameMode, players):

    global myFont, myFontLarge, WHITE
    
    widthDisplay = 800
    heightDisplay = 600

    gameDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("insert_names.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    getReadyMsg = myFontLarge.render(("GET READY !!!"), True, (WHITE))

    if gameMode == 1:
        player1 = players[0]
        gameModeMsg = myFontLarge.render(("SINGLE-PLAYER"), True, (WHITE))
        playersMsg = myFont.render((str(player1)), True, (WHITE))

    if gameMode == 2:
        player1 = players[0]
        player2 = players[1]
        gameModeMsg = myFontLarge.render(("MULTI-PLAYER"), True, (WHITE))
        playersMsg = myFont.render((str(player1) + " VS " + str(player2)), True, (WHITE))

    if gameMode == 4:
        gameModeMsg = myFontLarge.render(("ALL VS ALL"), True, (WHITE))
        playersMsg = myFont.render((" "), True, (WHITE))
        
        

    iniTime = time.time()
    timer = 0
    maxTime = 5            #Tiempo maximo para el juego en segundos
    while timer < maxTime:
        endTime = time.time()
        timer = endTime - iniTime

        timeLeftMsg = myFontLarge.render((str(int(maxTime - timer))), True, (WHITE))

        gameDisplay.blit(backgroundImage, (0,0))
        gameDisplay.blit(gameModeMsg, (widthDisplay//4, 25))
        gameDisplay.blit(getReadyMsg, (widthDisplay//4, 250))
        gameDisplay.blit(timeLeftMsg, (700,500))

        if gameMode == 1:
            gameDisplay.blit(playersMsg, (widthDisplay//2 - widthDisplay//4, 150))
        else:
            gameDisplay.blit(playersMsg, (widthDisplay//4, 150))


        pygame.display.update()

        
def firePower(playersList, playersCompleteInfo, mapPlayers):
    
    global myFont, myFontLarge, WHITE
    
    widthDisplay = 800
    heightDisplay = 800

    powerDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("fire_back.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))
    powerDisplay.blit(backgroundImage, (0,0))

    newOrderMsg = myFontLarge.render(("SEND TO START"), True, (50,50,50))
    powerDisplay.blit(newOrderMsg, (widthDisplay//4, 25))

    numOfPlayers = len(playersList)

    inScreen = True

    while inScreen:
        
        powerDisplay.blit(backgroundImage, (0,0))
        powerDisplay.blit(newOrderMsg, (widthDisplay//4, 25))

        for player in range(numOfPlayers):
            playerMsg = myFont.render((str(playersList[player])), True, (50,50,50))
            if player < 2:
                powerDisplay.blit(playerMsg, (((player + 1) * widthDisplay//6) + (player * widthDisplay//3), (heightDisplay//3)))
            elif player >= 2:
                powerDisplay.blit(playerMsg, (((player - 1) * widthDisplay//6) + ((player - 2) * widthDisplay//3), (heightDisplay//2) + 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            print(event)

        if inArea(0,215,400,230,powerDisplay):
            powerDisplay.blit(playersCompleteInfo[playersList[0]][0], (115,165))
            if buttonInGameVer2(0,215,400,230,powerDisplay):
                playerName = playersList[0]
                currentPos = playersCompleteInfo[playerName][3]
                mapPlayers[currentPos].remove(playerName)
                mapPlayers[0] += [playerName]
                playersCompleteInfo[playerName][3] = 0
                inScreen = False

        if inArea(400,215,400,230,powerDisplay):
            powerDisplay.blit(playersCompleteInfo[playersList[1]][0], (515,165))
            if buttonInGameVer2(400,215,400,230,powerDisplay):
                playerName = playersList[1]
                currentPos = playersCompleteInfo[playerName][3]
                mapPlayers[currentPos].remove(playerName)
                mapPlayers[0] += [playerName]
                playersCompleteInfo[playerName][3] = 0
                inScreen = False

        if numOfPlayers > 2:                
            if inArea(0,445,400,335,powerDisplay):
                powerDisplay.blit(playersCompleteInfo[playersList[2]][0], (115,430))
                if buttonInGameVer2(0,445,400,335,powerDisplay):
                    playerName = playersList[2]
                    currentPos = playersCompleteInfo[playerName][3]
                    mapPlayers[currentPos].remove(playerName)
                    mapPlayers[0] += [playerName]
                    playersCompleteInfo[playerName][3] = 0
                    inScreen = False

        if numOfPlayers > 3:                
            if inArea(400,445,400,335,powerDisplay):
                powerDisplay.blit(playersCompleteInfo[playersList[3]][0], (515,430))
                if buttonInGameVer2(400,445,400,335,powerDisplay):
                    playerName = playersList[3]
                    currentPos = playersCompleteInfo[playerName][3]
                    mapPlayers[currentPos].remove(playerName)
                    mapPlayers[0] += [playerName]
                    playersCompleteInfo[playerName][3] = 0
                    inScreen = False


        pygame.display.update()
              
    pygame.time.wait(200)
    return


def icePower(playersList, playersCompleteInfo):
    
    global myFont, myFontLarge, WHITE
    
    widthDisplay = 800
    heightDisplay = 800

    powerDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))

    backgroundImage = pygame.image.load("ice_back.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))
    powerDisplay.blit(backgroundImage, (0,0))

    newOrderMsg = myFontLarge.render(("FREEZE A PLAYER"), True, (50,50,50))
    powerDisplay.blit(newOrderMsg, (widthDisplay//4, 25))

    numOfPlayers = len(playersList)

    inScreen = True

    while inScreen:
        
        powerDisplay.blit(backgroundImage, (0,0))
        powerDisplay.blit(newOrderMsg, (widthDisplay//4, 25))

        for player in range(numOfPlayers):
            playerMsg = myFont.render((str(playersList[player])), True, (50,50,50))
            if player < 2:
                powerDisplay.blit(playerMsg, (((player + 1) * widthDisplay//6) + (player * widthDisplay//3), (heightDisplay//3)))
            elif player >= 2:
                powerDisplay.blit(playerMsg, (((player - 1) * widthDisplay//6) + ((player - 2) * widthDisplay//3), (heightDisplay//2) + 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            print(event)

        if inArea(0,215,400,230,powerDisplay):
            powerDisplay.blit(playersCompleteInfo[playersList[0]][0], (115,165))
            if buttonInGameVer2(0,215,400,230,powerDisplay):
                playerName = playersList[0]
                playersCompleteInfo[playerName][2] += 2
                inScreen = False

        if inArea(400,215,400,230,powerDisplay):
            powerDisplay.blit(playersCompleteInfo[playersList[1]][0], (515,165))
            if buttonInGameVer2(400,215,400,230,powerDisplay):
                playerName = playersList[1]
                playersCompleteInfo[playerName][2] += 2
                inScreen = False

        if numOfPlayers > 2:                
            if inArea(0,445,400,335,powerDisplay):
                powerDisplay.blit(playersCompleteInfo[playersList[2]][0], (115,430))
                if buttonInGameVer2(0,445,400,335,powerDisplay):
                    playerName = playersList[2]
                    playersCompleteInfo[playerName][2] += 2
                    inScreen = False

        if numOfPlayers > 3:                
            if inArea(400,445,400,335,powerDisplay):
                powerDisplay.blit(playersCompleteInfo[playersList[3]][0], (515,430))
                if buttonInGameVer2(400,445,400,335,powerDisplay):
                    playerName = playersList[3]
                    playersCompleteInfo[playerName][2] += 2
                    inScreen = False


        pygame.display.update()
              
    pygame.time.wait(200)
    return

def finalWinnerScreen(winnerPlayer):
    
    global myFont, myFontLarge, BLACK, WHITE

    myFontLarger = pygame.font.SysFont("Segoe UI Black", 49)
    
    widthDisplay = 1300
    heightDisplay = 800

    menuPrincipalDisplay = pygame.display.set_mode((widthDisplay,heightDisplay))
    clock = pygame.time.Clock()
    

    backgroundImage = pygame.image.load("menuPrincipal2.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (widthDisplay, heightDisplay))

    playAgainMsg = myFont.render(("PLAY AGAIN"), True, (BLACK))
    winnerMsg = myFontLarge.render(("CONGRATULATIONS"), True, (BLACK))
    winnerMsg2 = myFontLarge.render(("YOU WIN: " + str(winnerPlayer)), True, (BLACK))
    winnerMsgBack = myFontLarger.render(("CONGRATULATIONS"), True, (WHITE))
    winnerMsg2Back = myFontLarger.render(("YOU WIN: " + str(winnerPlayer)), True, (WHITE))


    inMenu = True

    while inMenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        menuPrincipalDisplay.blit(backgroundImage, (0,0))
        menuPrincipalDisplay.blit(playAgainMsg, ((widthDisplay//2) - (widthDisplay//12), 600))
        menuPrincipalDisplay.blit(winnerMsgBack, ((widthDisplay//2) - (widthDisplay//6), 250))
        menuPrincipalDisplay.blit(winnerMsg2Back, ((widthDisplay//2) - (widthDisplay//7), 400))
        menuPrincipalDisplay.blit(winnerMsg, ((widthDisplay//2) - (widthDisplay//6), 250))
        menuPrincipalDisplay.blit(winnerMsg2, ((widthDisplay//2) - (widthDisplay//7), 400))
        


        if buttonInGame(((widthDisplay//2) - (widthDisplay//12)), 600, 230, 50, menuPrincipalDisplay, 230, -3):
            return menuPrincipal()

        pygame.display.update()
        
        clock.tick(60)

    
mal = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

##startGameGsThePath([[0,0,0],
##               [0,0,0],
##               [0,0,0],
##               [0,0,0],
##               [0,0,0],
##               [0,0,0],
##               [0,0,0],
##               [0,0,0]], sanjiPiece)


#startGameTicTacToe([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], sanjiPiece, luffyPiece)

def hacer():

    newList = []

    for i in range(18):
        newList += ["game" + str(i+1)]

    return newList

def formMatrix(numRows, numCol):

    newRow = []

    newMatrix = []
    
    for i in range(numCol):
        newRow += [0]

    for j in range(numRows):
        insertRow = list(newRow)
        newMatrix += [insertRow]

    return newMatrix
        
        

def printMatrix(matrix):

    for i in matrix:
        print(*i)


menuPrincipal()
