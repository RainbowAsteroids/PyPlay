import pygame

gameExit = False
displayWidth = 800
displayHeight = 600
blockSize = 10
pink = [255,13,255]
black = [0,0,0]
version = False
dots = {
    "heart":[],
    "square":[]
}
FPS = 20
shape = "square"

for i in range(150, 660, 10):
    dots["square"] = dots["square"]+[[i,150]]
for i in range(150, 460, 10):
    dots["square"] = dots["square"]+[[650,i]]
for i in range(650,140,-10):
    dots["square"] = dots["square"]+[[i,450]]
for i in range(450,140,-10):
    dots["square"] = dots["square"]+[[150,i]]


pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Drawing!")
font = pygame.font.SysFont(None, 25)


def draw(shape):
    gameDisplay.fill(black if not version else pink)
    for i in range(len(dots[shape])):
        pygame.draw.rect(gameDisplay, pink if not version else black, dots["square"][i]+[blockSize, blockSize])
        pygame.display.update()
        clock.tick(FPS)
    printText("Press S to draw a square!",pink if not version else black, [displayWidth/2, displayHeight/2])
    printText("Press any other letter to replay the animation!",pink if not version else black, [displayWidth/2, displayHeight/2+30])
def textObjects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def printText(msg,color,cords):
    textSurf, textRect = textObjects(msg,color)
    """
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, cords)
    pygame.display.update()"""
    textRect.center = (cords[0]), (cords[1])
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

draw(shape)
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                version = False
                shape = "square"
            else:
                version = not version
            draw(shape)
