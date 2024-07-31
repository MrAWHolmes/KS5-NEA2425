#-------------------------------------------------------------------------------
# Name:        pygame-tut01
# REF : https://youtu.be/i6xMBig-pP4?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
# REF2: https://www.pygame.org/docs/ref/pygame.html#pygame.init
#-------------------------------------------------------------------------------

import pygame


def start(width,height,caption)->pygame.Surface:
    #initi pygame
    pygame.init()

    size_tuple = (width,height)
    win = pygame.display.set_mode(size_tuple)

    pygame.display.set_caption(caption)

    return win

def drawRedRec(x:int,y:int,width:int,height:int,colour:tuple=(255,0,0)):
    pygame.draw.rect(win,colour,(x,y,width,height))


def main_loop(delay_ms):
    run = True

    while run:
        pygame.time.delay(delay_ms)

        #event handler loop here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #updated screen frames here <--
        # apply chhanges to win surface <---
        drawRedRec(50,50,40,20)


        #call display.update() to render new frame
        pygame.display.update()

def stop():
    pygame.quit()

def main():
    global win

    win = start(800,600,"title") #SVGA : 800x600

    main_loop(100)

    stop()

if __name__ == '__main__':
    main()

