#-------------------------------------------------------------------------------
# Name:        pygame-tut01-oop
# REF : https://youtu.be/i6xMBig-pP4?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
# REF2: https://www.pygame.org/docs/ref/pygame.html#pygame.init
#-------------------------------------------------------------------------------

import pygame

class gfxObject:
    id         : str = None
    pos_size   : pygame.Rect = None
    attributes : None
    surface    : None
    key_binds  : None


    def __init__(self,stringId:str,x:int,y:int,w:int,h:int):
        self.id = stringId
        self.pos_size = pygame.Rect(x,y,w,h)
        self.attributes = {} #custom associative array of attributes {attrib:value}
        self.key_binds = {}


    def addAttrib(self,anAtribute,aValue):
        self.attributes[anAttribute] = aValue

    def setSurface(self,win):
        self.surface = pygame.draw.rect(win,(255,0,0),self.pos_size)

    def getAttrib(self,anAttribute):
        if anAttribute in self.attributes:
            return self.attributes[anAttribute]
        else:
            return None

    def add_key_bind(self,dirStr,pygameKey):
        self.key_binds[dirStr] = pygameKey

    def handleKeyMovement(self,keys):
        dx = 0
        dy = 0
        speed= 10

        for keyId in self.key_binds:
            if keyId == "left" and keys[self.key_binds[keyId]]:
                dx = -1 * speed
            if keyId == "right" and keys[self.key_binds[keyId]]:
                dx =  1 * speed

        return dx,dy


    def update(self,dx,dy):
        (x,y,w,h) = self.pos_size

        self.pos_size = pygame.Rect(x+dx,y+dy,w,h)

    def draw(self,win):
        self.setSurface(win)




class World:
    win = None
    run = True
    delay_ms = None

    gfxObjects = None

    def __init__(self,width,height,caption,delay_ms=100):
        self.start(width,height,caption)
        self.delay_ms = delay_ms

        self.gfxObjects = {} # store gfx objects with an id
                             # Add fgxObjects with addObject
                             # Remove with popObject

    def addObject(self,anObject):
        self.gfxObjects[anObject.id] = anObject

    def popObject(self,anObjectId:str):
        pass

    def start(self,width,height,caption)->pygame.Surface:
        #initi pygame
        pygame.init()

        size_tuple = (width,height)
        self.win = pygame.display.set_mode(size_tuple)

        pygame.display.set_caption(caption)

    def loop(self):
        keys = pygame.key.get_pressed()

        for id in self.gfxObjects:
            dx,dy=self.gfxObjects[id].handleKeyMovement(keys)
            self.gfxObjects[id].update(dx,dy)
            self.gfxObjects[id].draw(self.win)


    def main_loop(self):
        self.run = True

        while self.run:
            #clear current frame
            self.win.fill((0,0,0))

            pygame.time.delay(self.delay_ms)

            #event handler loop here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.loop()  # calls .update() and .draw()

            pygame.display.update()

    def stop(self):
        pygame.quit()

def main():
    redRect = gfxObject("redRect",50,50,40,30)
    redRect.add_key_bind("left",pygame.K_a)
    redRect.add_key_bind("right",pygame.K_d)

    w = World(800,600,"title") #SVGA : 800x600
    w.addObject(redRect)

    w.main_loop()
    w.stop()

if __name__ == '__main__':
    main()

