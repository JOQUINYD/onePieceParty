import os
import pygame
import random

pygame.init()

BLACK = (0,0,0)

screen = pygame.display.set_mode((1600, 960))

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


##def defineCards():
##
##    cardsPack = load_images(path_to_directory)
##
##    keyList = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'EC', 'ED', 'EH', 'ES', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS', 'ZAC', 'ZAD', 'ZAH', 'ZAS']
##
##    for key in keyList:
##        image = cardsPack.get(key)
##        image = pygame.transform.scale(image, (100,150))
##


def show(screen):

    cardsPack = load_images(path_to_directory)

    keyList = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'EC', 'ED', 'EH', 'ES', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS', 'ZAC', 'ZAD', 'ZAH', 'ZAS']

##    print(list(cards.keys()))    
    widthDisplay = 1600
    heightDisplay = 960
    
    random.shuffle(keyList)
    
    newMatrix = []
    for i in range(6):
        newRow = []
        for j in range(7):
            newRow += [keyList[i*7 + j]]
        newMatrix += [newRow]

    print(newMatrix)
     
    drawBoardCards(newMatrix, screen, widthDisplay, heightDisplay, cardsPack)

    pygame.display.update()
    

def drawBoardCards(board, screen, widthDisplay, heightDisplay, cardsPack):

    numRows = len(board)
    numColumns = len(board[0])

    posXmark = (widthDisplay//3)
    posYmark = (heightDisplay//3)
        
    for r in range(numRows):
        for c in range(numColumns):
            posXmark = (c*(widthDisplay//7)) + 15
            posYmark = r*(heightDisplay//8)
            print(board[r][c])
            image = cardsPack.get(board[r][c])
            image = pygame.transform.scale(image, (100,150))
            screen.blit(image, (int(posXmark), int(posYmark)))
            pygame.display.update()
    
    pygame.display.update()



def arrastrar(screen):

    global BLACK

    imagen = pygame.image.load("2D.png")
    imagen = pygame.transform.scale(imagen, (50,50))

    gameOver = False
    
    while not gameOver:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            while event.type == pygame.MOUSEBUTTONDOWN:

                screen.fill(BLACK)

                for event in pygame.event.get():
                    posx = event.pos[0]
                    posy = event.pos[1]

                    screen.blit(imagen, (posx, posy))
                    pygame.display.update()


def gsThePathGame(matrix, player, lives = 5, path = 7):

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
                            return gsThePathGame(originalMatrix, player, lives - 1, 7)

        drawBoardGsThePath(matrix, gsThePathDisplay, widthDisplay, heightDisplay, lives)

        pygame.display.update()

        if lives == 0:
            win = False
            gameOver = True
            

        if path == -1:
            win = True
            gameOver = True
            
    if gameOver:
        if win:
            pygame.time.wait(3500)
            winnerScreen(player)
        return

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
            







def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])



















