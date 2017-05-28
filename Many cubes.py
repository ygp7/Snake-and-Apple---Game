import pygame

pygame.init() #initializes module things

red = (255,0,0) #bleh not used anywhere
gamescreen = pygame.display.set_mode((850,650))
pygame.display.set_caption("Baba")
#pygame.display.update()  //When we are completely done with all the actions then we will write this command for rendering

x = True
y = 0
c = 0
i = 0
while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False
        #print event

    gamescreen.fill((255,0,0))
    while y!= 25:
        pygame.draw.rect(gamescreen,(255 - c,255 ,0),(10 + i,10 ,40,40))
        i = i + 50
        c = c+10
        y = y + 1
        pygame.display.update()
pygame.quit()
quit()
