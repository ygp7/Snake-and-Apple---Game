import pygame
import time
import random

pygame.init() #initializes modules
red = (255,0,0) #bleh not used anywhere


#dimensions of the screen
disp_width = 1000
disp_height = 500

appleimg = pygame.image.load("chhotuapple.png")

icon = pygame.image.load("snakehead.png")
pygame.display.set_icon(icon)
gamescreen = pygame.display.set_mode((disp_width,disp_height)) #Makes the screen
pygame.display.set_caption("SNAKESSSSSSSS") #name of screen window


img = pygame.image.load('snakehead.png')

pygame.display.update()  #//When we are completely done with all the actions then we will write this command for rendering

FPS = 30 #frame per second with which our screen is rendered

move_step = 10
block_size = move_step*2
clock = pygame.time.Clock() #for fps
coinsize = 50
direction = "right"


#function for displaying the message on the screen
def message(msg,color,fontsize,widthratio,heightratio,fontname = "Arial"):
    font = pygame.font.SysFont("arial" ,fontsize)             #fonts for displaying text on screen
    screen_text = font.render(msg,True,color)
    gamescreen.blit(screen_text,[disp_width/widthratio,disp_height/heightratio])

def snake(block_size,snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img,270)

    if direction == "left":
        head = pygame.transform.rotate(img,90)

    if direction == "up":
        head = pygame.transform.rotate(img,0)

    if direction == "down":
        head = pygame.transform.rotate(img,180)


    for XnY in snakelist:
        pygame.draw.rect(gamescreen,(63, 72, 204),[XnY[0] ,XnY[1] ,block_size,block_size])
        gamescreen.blit(head, (snakelist[-1][0], snakelist[-1][1]))


def mainscreen():

    intro = True
    while intro == True:

        gamescreen.fill((110,125,244))
        message("  Welcome to SNAKESSS!",(0,0,150),45,4.5,80,"segoescript")
        message("INSTRUCTIONS:",(255,5,25),50,80,4.5,"Regular")
        message("1.Objective is to eat all the apples.",(0,0,0),25,80,2.9,"Regular")
        message("2.You grow longer as you eat more apples",(0,0,0),25,80,2.5,"Regular")
        message("3.If you run into yourself or into edges of the screen,You die!",(0,0,0),25,80,2.18,"Regular")
        message("Press C to continue or press Q to quit.",(55,0,155),35,20,1.5,"consolas")
        message("Press P to pause while playing the game.",(55,0,155),20,20,1.3,"consolas")
        message("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
                "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",(10,50,0),20,700,1.05)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
        clock.tick(FPS/40)
def pause():
    pause = True
    while pause == True:
        #gamescreen.fill((250,250,0))
        message("PAUSED",(250,0,0),60,2.4,3.5)
        message(" Press 'P' to Proceed the game.",(0,0,0),30,2.9,1.9)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

    clock.tick(FPS/6)



#main gameloop
def gameloop():
    global direction
    x = True
    gameover = False
    xlead = disp_width/10
    ylead = disp_height/1.5
    xcont = 10
    ycont = 0
    score = 0
    move = 0

    randomecoinx = round(random.randrange(0,disp_width-coinsize))#/10.0)*10
    randomecoiny = round(random.randrange(0,disp_height-coinsize))#/10.0)*10
    randomecoinbox = round(random.randrange(0,disp_height-coinsize))#/10.0)*10
    snakelist = []

    snakelength = 1



#this while x loop works when x is true and contains the game
    while x:
        move = move +5
        while gameover == True:       #this loop is used after user out ho gayaa hai and now he wants to exit or continue
            gamescreen.fill((135,206,250))
            message("Game Over!!!",(255,10,10),70,3.8,10,"segoeprint")
            message("    To Play Again -> ",(100,55,210),35,4.5,1.5,"Regular")
            message("Press 'R'",(100,55,210),30,1.7,1.47,"Regular")
            message("    To Quit ->",(100,55,210),35,4.5,1.29,"Regular")
            message("Press 'Q'",(100,55,210),30,1.7,1.27,"Regular")
            message("SCORE:" + str(score),(0, 155, 38),80,3.5,3,"segoeprint")
            pygame.display.update()
#for loop for event handeling after user out ho jaata hai
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        x = False
                        gameover = False
                    if event.key == pygame.K_r:
                        direction = "right"
                        gameloop()
#for loop for event handeling for movement and quitting the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
                gameover = False
            #print event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xcont =-move_step
                    ycont = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    xcont = move_step
                    ycont = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    ycont = -move_step
                    xcont = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    ycont = move_step
                    xcont = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                    pause()
#Taaki key uthate hi ruk jaaye motion
            #if event.type == pygame.KEYUP:
             #   if event.key == pygame.K_LEFT:
              #      xcont = 0

               # elif event.key == pygame.K_RIGHT:
                #    xcont = 0

                #elif event.key == pygame.K_UP:
                 #   ycont = 0
                #elif event.key == pygame.K_DOWN:
                 #   ycont = 0
#Motion badhega xcont se,xlead position hai object ki
        xlead +=xcont
        ylead +=ycont

#Boundries
        if xlead > disp_width - block_size or xlead < 0 or ylead > disp_height - block_size or ylead < 0:
            gameover = True

        gamescreen.fill((250,250,0))
        #pygame.draw.rect(gamescreen,(255,0,0),[randomecoinx,randomecoiny,coinsize,coinsize])

        gamescreen.blit(appleimg, (randomecoinx,randomecoiny))
        snake(block_size,snakelist)
        message("Score:" + str(score),(255,0,0),20,900,400,"comicsansms")

        #pygame.draw.rect(gamescreen,(255,0,0),[0+move,randomecoinbox,coinsize,coinsize])
        #if move >= disp_width:
        #    move = 0
        #   randomecoinbox = round(random.randrange(0,disp_height-coinsize))#/10.0)*10

        #   pygame.draw.rect(gamescreen,(255,0,0),[0+move,randomecoinbox,coinsize,coinsize])
        pygame.display.update()

        snakehead = []
        snakehead.append(xlead)
        snakehead.append(ylead)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover = True

#Apple colission code
        # if xlead >= randomecoinx and  xlead <= randomecoinx + applesize:
        #     if ylead >= randomecoiny and  ylead <= randomecoiny + applesize:
        #         randomecoinx = round(random.randrange(0,disp_width-block_size))# /10.0)*10.0
        #         randomecoiny = round(random.randrange(0,disp_height-block_size))# /10.0)*10.0
        #         snakelength += 1

        # if xlead == randomecoinx and ylead == randomecoiny:
        #     randomecoinx = round(random.randrange(0,disp_width-block_size)/10.0)*10.0
        #     randomecoiny = round(random.randrange(0,disp_height-block_size)/10.0)*10.0
        #     snakelength += 1

#Modified apple colission code
        if xlead > randomecoinx and xlead < randomecoinx + coinsize or xlead + block_size > randomecoinx and xlead + block_size < randomecoinx + coinsize:
            if ylead > randomecoiny and ylead < randomecoiny + coinsize or ylead + block_size > randomecoiny and ylead + block_size < randomecoiny + coinsize:
                randomecoinx = round(random.randrange(0,disp_width-coinsize))# /10.0)*10.0
                randomecoiny = round(random.randrange(0,disp_height-coinsize))# /10.0)*10.0
                snakelength += 1
                score += 10




        clock.tick(FPS)

    pygame.quit()
    quit()

mainscreen()
gameloop()