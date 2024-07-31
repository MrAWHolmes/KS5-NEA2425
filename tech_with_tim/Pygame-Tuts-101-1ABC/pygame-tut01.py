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

def main_loop(delay_ms):
    run = True

    while run:
        pygame.time.delay(delay_ms)

        #event handler loop here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def stop():
    pygame.quit()

def main():

    win = start(800,600,"title") #SVGA : 800x600

    main_loop(100)

    stop()

if __name__ == '__main__':
    main()


class oopPygame:
    self.win = None


    def start(self,width,height):
        pygame.init()
        win = pygame.display.set_mode(width,height)
        return win



    def stop(self):
        pygame.quit()
