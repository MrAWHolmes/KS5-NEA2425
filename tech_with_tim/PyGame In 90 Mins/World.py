import pygame
import os

class HashQ:
    Q = None
    X = None

    def __init__(self):
        self.Q = dict()

    def addNode(self,name,anyObject):
        if name not in self.Q:
            self.Q[name] = list()
        self.Q[name].append(anyObject)
    
    def delNode(self,name):
        if name in self.Q:
            try:
                del this.Q[name]
            except:
                this.X.append(name)    


    
class World:
    COLOURS = None
    WIN = None
    GfxQ = None
    EventsQ = None
    FPS = None

    def __init__(self,width:int,height:int,title:str,fps:int=60):
        """
        Some defualt colour tuples...
        """
        World.COLOURS = dict()
        World.COLOURS["BLACK"] = (0,0,0)
        World.COLOURS["WHITE"] = (255,255,255)
        World.COLOURS["RED"] = (255,0,0)
        World.COLOURS["GREEN"] = (0,255,0)
        World.COLOURS["BLUE"] = (0,0,255)

        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(title)

        GfxQ = dict()
        EventsQ = dict()


        pygame.font.init()
        pygame.mixer.init()



    def drawWindow(self):
        """

        """
        self.WIN.fill(self.COLOURS["BLACK"])

        for gfxObject in GfxQ:
            if hasattr(gfxObject,'draw'):
                gfxObject.draw()

        pygame.display.update()

    def joinGfxQ(self,name:str,GfxObj):
        self.GfxQ[name] = GfxObj

    def leaveGfxQ(self,name):
        if not hasattr(self,"exitQ"):
            self.exitQ = list()
        self.exitQ.append(name)


    def main_loop(self,FPS:int):

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



def main():
    startPygame()


if __name__ == "__main__":
    main()
