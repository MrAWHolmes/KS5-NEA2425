import pygame
import os

class GfxQueNode:
    ptr = None  # pointer to a object
    id  = int() # nodes integer id


class GfxQue:



class World:
    WIN = None
    gfxObjQueue = None

    def __init__(self,w,h,bgColour,bgImage=None):
        pygame.font.init()
        pygame.mixer.init()



def startPygame():


    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("First Game!")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    gfxObjectList = list()





def draw_window(GfxObjectList:list):
    """

    """
    WIN.fill(BACK)

    for gfxObject in GfxObjectList:
        if hasattr(gfxObject,'draw'):
            gfxObject.draw()

    pygame.display.update()



def main_loop(FPS:int,GfxObjectList:list):

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                for gfxObject in gfxObjectList:
                    if hasattr(fgxObject,'grabKeydown'):
                        fgxObject.grabKeydown(event)

        keys_pressed = pygame.key.get_pressed()


        draw_window(gfxObjectList)

def addGfxObject(gfxObject):
    global GfxObjectList


def main():
    startPygame()


if __name__ == "__main__":
    main()
