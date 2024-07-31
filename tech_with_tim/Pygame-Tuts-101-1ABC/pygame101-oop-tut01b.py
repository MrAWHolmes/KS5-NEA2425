#-------------------------------------------------------------------------------
# Name:        pygame-tut01-oop
# REF : https://youtu.be/i6xMBig-pP4?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
# REF2: https://www.pygame.org/docs/ref/pygame.html#pygame.init
#-------------------------------------------------------------------------------

import pygame

class GfxObject:
    id         : str = None                 # each object needs a string key
    pos_size   : pygame.Rect = None         # tuple (x,y, width, height)
    attributes : None                       # dictionary of attributes
    surface    : None                       # pygame.Surface graphical repr.


    def __init__(self,stringId:str,x:int,y:int,w:int,h:int):
        """
          constructor __init__(stringId:str,x:int,y:int,w:int,h:int)

          stringId : must be an unique non-null name
          x,y      : top left position in (x,y)
          w,h      : (width,height)

        """
        self.id = stringId
        self.pos_size = pygame.Rect(x,y,w,h)
        self.attributes = {} #custom associative array of attributes {attrib:value}

    def width(self)->int:
        """
         getter : Surface width
        """
        return self.pos_size[2]

    def height(self)->int:
        """
         getter : Surface height
        """
        return self.pos_size[3]

    def addAttribute(self,anAtribute:str,aValue:any):
        """
          addAttribute(anAtribute:str,aValue:any)
          example addAttribute("alive",True)
        """
        self.attributes[anAttribute] = aValue

    def setAttribute(self,anAtribute:str,aValue:any):
        """
          setAttribute(anAtribute:str,aValue:any)
          example addAttribute("alive",False)
          WARNING! Will create if DNE
        """
        self.attributes[anAttribute] = aValue

    def getAttribute(self,anAttribute:str)->any: #None if dne
        """
        safe Getter of an attribute value.
        Returns attribute value or None if no matching attribute/no value set
        """
        if anAttribute in self.attributes:
            return self.attributes[anAttribute]
        else:
            return None

    def setSurface(self,newSurface:pygame.Surface):
        """
          Set the GfxObjects.surface attribute
        """
        self.surface = newSurface

    def update(self,dx,dy):
        (x,y,w,h) = self.pos_size
        #print(x,y,w,h)
        self.pos_size = pygame.Rect(x+dx,y+dy,w,h)

    def draw(self,win:pygame.Surface):
        win.blit(self.surface,self.pos_size[:2])


class World:
    # treat all attributes as private.
    # not using __win etc as annoying!
    win = None        # the pygame.Surface that is the main window
    run = True        # flag controlling the main pygame while loop
    delay_ms = None   # pause in ms used by pygame.time.delay() in main loop

    gfxObjects = None # dictionary of graphic objects that loop() will render

    def __init__(self,width:int,height:int,caption:str,delay_ms:int=100):
        """
        constructor:
         __init__(width:int,height:int,caption:str,delay_ms:int=100)

         sets window width and height and window caption by calling start()

         set delay in ms (default 100) to pause between frames of main loop

        """
        self.start(width,height,caption)
        self.delay_ms = delay_ms

        self.gfxObjects = {} # store gfx objects with an id
                             # Add fgxObjects with addObject
                             # Remove with popObject

    def addObject(self,anObject):
        """
         adds a GfxObject to the dictionary gfxObjects
         used by loop() to iterate over .update() and .draw()
         no safety code - may implement if it becomes necessary
        """
        self.gfxObjects[anObject.id] = anObject

    def popObject(self,anObjectId:str):
        """
         will be implemented later - safety code required so can be queued
          for removal and only executed after iterable dictionary loop is done.

        """
        pass

    def start(self,width:int,height:int,caption:str)->pygame.Surface:
        """
        private function start(width:int,height:int,caption:str)->pygame.Surface
        returns a pygame.Surface window

        sets window width and height and window caption

        """
        #initi pygame
        pygame.init()

        size_tuple = (width,height)
        self.win = pygame.display.set_mode(size_tuple)

        pygame.display.set_caption(caption)

    def loop(self):
        """
        Iterates through all graphics objects
        Calls each graphic objects update() and draw() methods

        At this stage we auto update by moving right
        """
        for id in self.gfxObjects:
            # event hamdlers will be called here ... this will control dx,dy of update()
            self.gfxObjects[id].update(3,0)     # automatically move right to test...
            self.gfxObjects[id].draw(self.win)  # draw on the world window Surface

    def main_loop(self):
        """
         Runs the main game loop using the delay_ms value.

         Exits correctly when exit is selected.

         Calls loop() which handles each gfxObject update() and draw() method
        """
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

def drawRedFigure(width,height)->pygame.Surface:
    # draw rectangle and grab it from surface2
    # in practice this would be an image
    surface2=pygame.Surface((width,height))
    pygame.draw.rect(surface2,(255,0,0),(0,0,width,height))
    pygame.draw.line(surface2,(0,0,0),(15,15),(30,15),3)

    return surface2


def main():
    world=World(800,600,"world-oop101b") #SVGA : 800x600

    redFig = GfxObject("redFigure",50,50,30,40) #create red rectangle object

    redFig.setSurface(drawRedFigure(redFig.width(),redFig.height()))

    world.addObject(redFig)                      # insert it into the world

    world.main_loop()                            # run main game loop until
                                                 # quit selected...
    world.stop()

if __name__ == '__main__':
    main()

