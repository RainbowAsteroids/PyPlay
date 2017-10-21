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
FPS = 10

for i in range(150, 660, 10):
    dots["square"] = dots["square"]+[[i,150]]
for i in range(150, 460, 10):
    dots["square"] = dots["square"]+[[650,i]]
for i in range(650,140,-10):
    dots["square"] = dots["square"]+[[i,450]]
for i in range(450,140,-10):
    dots["square"] = dots["square"]+[[150,i]]
print(dots["square"])


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
    printText("Press any key to restart animation!",pink if not version else black)
def printText(msg,color):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth/2, displayHeight/2])
    pygame.display.update()

draw("square")
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            version = not version
            draw("square")
