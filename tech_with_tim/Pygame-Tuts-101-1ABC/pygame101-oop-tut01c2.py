#-------------------------------------------------------------------------------
# Name:        pygame-tut01-oop
# REF : https://youtu.be/i6xMBig-pP4?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
# REF2: https://www.pygame.org/docs/ref/pygame.html#pygame.init
#-------------------------------------------------------------------------------

import pygame


class GfxObject:
    id: str = None                  # each object needs a string key
    pos_size: pygame.Rect = None    # tuple (x,y, width, height)
    attributes: dict = None         # dictionary of attributes {att:value}
    surface: pygame.Surface = None  # pygame.Surface graphical repr.
    key_binds: dict = None          # dictionary of keys {keyId:[pygame.key_values]}

    def __init__(self, stringId: str, x: int, y: int, w: int, h: int):
        """
          constructor __init__(stringId:str,x:int,y:int,w:int,h:int)

          stringId : must be an unique non-null name
          x,y      : top left position in (x,y)
          w,h      : (width,height)

        """
        self.id = stringId
        self.pos_size = pygame.Rect(x, y, w, h)
        self.attributes = {}        # custom associative array of attributes {attrib:value}
        self.key_binds = {}         # custom associative array of key binds {keyString : []}

    def width(self) -> int:
        """
         getter : Surface width
        """
        return self.pos_size[2]

    def height(self) -> int:
        """
         getter : Surface height
        """
        return self.pos_size[3]

    def getPos(self) -> tuple :
        """"
          getter
          :return (x,y) position tuple

        """
        return self.pos_size[:2] # return (x,y)

    def setPos(self,newX:int,newY:int)->None:
        """
        Setter - changes (x,y) to (newX, newY)
        :param newX: int
        :param mnewY: int
        :return: None
        """
        self.pos_size = (newX,newY,self.pos_size[2],self.pos_size[3])

    def addAttribute(self, anAtribute: str, aValue: any):
        """
          addAttribute(anAtribute:str,aValue:any)
          example addAttribute("alive",True)
        """
        self.attributes[anAttribute:str] = aValue

    def setAttribute(self, anAtribute: str, aValue: any):
        """
          setAttribute(anAtribute:str,aValue:any)
          example addAttribute("alive",False)
          WARNING! Will create if DNE
        """
        self.attributes[anAttribute:str] = aValue

    def getAttribute(self, anAttribute: str) -> any:  #None if dne
        """
        safe Getter of an attribute value.
        Returns attribute value or None if no matching attribute/no value set
        """
        if anAttribute in self.attributes:
            return self.attributes[anAttribute]
        else:
            return None

    def setSurface(self, newSurface: pygame.Surface):
        """
          Set the GfxObjects.surface attribute
        """
        self.surface = newSurface

    def update(self, dx, dy):
        """
         moves the GfxObject by updating its (x,y) position
        """
        (x, y, w, h) = self.pos_size
        #print(x,y,w,h)
        self.pos_size = pygame.Rect(x + dx, y + dy, w, h)

    def draw(self, win: pygame.Surface):
        """
         draws the Surface "image" at positon (x,y)
        """
        win.blit(self.surface, self.pos_size[:2])  # (x,y)=(pos_size[0],pos_size[1])

    def getKeyIdStrings(self)->list:
        """genrates keyIdStr
           Most actions provided
           Can add to this list if more are required.
        """
        keyIdStrings = ["left", "right", "up", "down", "jump", "fire", "fire2", "use", "duck"]
        return keyIdStrings

    def add_key_bind(self, keyIdStr: str, pygameKey: int) -> bool:
        """
          Injects keyIdStr into dictionary key_binds
          keyIdStr : String key - eg "left"
          pygameKey : int : pygame.K_a for pressing "a"

          note: supports multiple binds supported - so cant do "left" as "pygame.K_LEFT"
          note: call getKeyIdStrings() to see valid keyIdStr values
        """
        #convert keyIdStr to all lower-case and strip white spaces
        keyIdStr = keyIdStr.lower()
        keyIdStr.replace(" ", "")

        validKeyIds = self.getKeyIdStrings()

        if not keyIdStr in validKeyIds:
            print(f"Warning! {keyIdStr} not in {validKeyIds}")
            print("add this keyIdString to the list in the method getKeyIdStrings()")
            print(f"Your keybind was not added to fgxObject {self.id}")
            return False

        # does the keyIdStr exist ion the dictionary yet?
        if not keyIdStr in self.key_binds:  #dne so create empty list for key binds
            self.key_binds[keyIdStr] = []

        # add key constant to keybind list
        self.key_binds[keyIdStr].append(pygameKey)
        return True

    def wasPressed(self, keyId:str, keys: pygame.key) -> bool:
        """
         helper function returns True if
           keyId matches some bind key in the list
        """
        if not keyId in self.getKeyIdStrings():
            print("wasPressed() warning!!!!")
            print(f"   Invalid keyId string '{keyId}' used'")
            print("    check handleKeyMovement() call is correct.")
            print("    check list in getKeyIdStrings() values.")
            return False

        pressed = False

        #iterate over list of bound keys and check if pressed
        for bind_key in self.key_binds[keyId]:
            pressed = pressed or keys[bind_key]

        return pressed

    def handleKeyMovement(self, keys: pygame.key, speed: int = 5):
        dx = 0
        dy = 0

        for keyId in self.key_binds:
            if keyId == "left" and self.wasPressed(keyId, keys):
                dx = -1 * speed

            if keyId == "right" and self.wasPressed(keyId, keys):
                dx = 1 * speed

            if keyId == "up" and self.wasPressed(keyId, keys):
                print("up pressed .. override to implement")
            if keyId == "down" and self.wasPressed(keyId, keys):
                print("down pressed .. override to implement")
            if keyId == "jump" and self.wasPressed(keyId, keys):
                print("jump pressed .. override to implement")
            if keyId == "fire2" and self.wasPressed(keyId, keys):
                print("fire2 pressed .. override to implement")
            if keyId == "duck" and self.wasPressed(keyId, keys):
                print("fire2 pressed .. override to implement")
            if keyId == "use" and self.wasPressed(keyId, keys):
                print("use pressed .. override to implement")

        return dx, dy


class World:
    # treat all attributes as private.
    # not using __win etc as annoying!
    win = None  # the pygame.Surface that is the main window
    run = True  # flag controlling the main pygame while loop
    delay_ms = None  # pause in ms used by pygame.time.delay() in main loop

    gfxObjects = None  # dictionary of graphic objects that loop() will render

    def __init__(self, width: int, height: int, caption: str, delay_ms: int = 100):
        """
        constructor:
         __init__(width:int,height:int,caption:str,delay_ms:int=100)

         sets window width and height and window caption by calling start()

         set delay in ms (default 100) to pause between frames of main loop

        """
        self.start(width, height, caption)
        self.delay_ms = delay_ms

        self.gfxObjects = {}  # store gfx objects with an id
        # Add fgxObjects with addObject
        # Remove with popObject

    def addObject(self, anObject: GfxObject):
        """
         adds a GfxObject to the dictionary gfxObjects
         used by loop() to iterate over .update() and .draw()
         no safety code - may implement if it becomes necessary
        """
        self.gfxObjects[anObject.id] = anObject

    def popObject(self, anObjectId: str):
        """
         will be implemented later - safety code required so can be queued
          for removal and only executed after iterable dictionary loop is done.

        """
        pass

    def start(self, width: int, height: int, caption: str) -> pygame.Surface:
        """
        private function start(width:int,height:int,caption:str)->pygame.Surface
        returns a pygame.Surface window

        sets window width and height and window caption

        """
        #initi pygame
        pygame.init()

        size_tuple = (width, height)
        self.win = pygame.display.set_mode(size_tuple)

        pygame.display.set_caption(caption)

    def loop(self):
        """
        Iterates through all graphics objects
        Calls each graphic objects update() and draw() methods

        At this stage we auto update by moving right
        """
        #get all keys pressed in this frame
        keys = pygame.key.get_pressed()

        for id in self.gfxObjects:
            # event hamdlers will be called here ... this will control dx,dy of update()
            dx, dy = self.gfxObjects[id].handleKeyMovement(keys, speed=5)
            self.gfxObjects[id].update(dx, dy)  # automatically move right to test...
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
            self.win.fill((0, 0, 0))

            pygame.time.delay(self.delay_ms)

            #event handler for QUIT here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.loop()  # calls .update() and .draw()

            pygame.display.update()

    def stop(self):
        pygame.quit()


def drawRedFigure(width, height) -> pygame.Surface:
    # draw rectangle and grab it from surface2
    # in practice this would be an image
    surface2 = pygame.Surface((width, height))
    pygame.draw.rect(surface2, (255, 0, 0), (0, 0, width, height))
    pygame.draw.line(surface2, (0, 0, 0), (15, 15), (30, 15), 3)

    return surface2


def main():
    """
    setup main game and populate game loop here using the World object

    """
    world = World(800, 600, "world-oop101c2")  #SVGA : 800x600

    redFig = GfxObject("redFigure", 50, 50, 30, 40)  #create red rectangle object

    redFig.setSurface(drawRedFigure(redFig.width(), redFig.height()))

    #print(redFig.getKeyIdStrings())

    ##    #add key binds for gfxObject - note A and left arrow!
    redFig.add_key_bind("left", pygame.K_a)
    redFig.add_key_bind("left", pygame.K_LEFT)
    redFig.add_key_bind("right", pygame.K_d)


    world.addObject(redFig)  # insert it into the world

    world.main_loop()  # run main game loop until
    # quit selected...
    world.stop()


if __name__ == '__main__':
    main()
