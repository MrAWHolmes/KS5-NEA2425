#-------------------------------------------------------------------------------
# Name:        pygame-tut01-oop
# REF : https://youtu.be/i6xMBig-pP4?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
# REF2: https://www.pygame.org/docs/ref/pygame.html#pygame.init
#-------------------------------------------------------------------------------

import pygame

class World:
    # treat all attributes as private.
    # not using __win etc as annoying!
    win = None        # the pygame.Surface that is the main window
    run = True        # flag controlling the main pygame while loop
    delay_ms = None   # pause in ms used by pygame.time.delay() in main loop

    def __init__(self,width:int,height:int,caption:str,delay_ms:int=100):
        """
        constructor:
         __init__(width:int,height:int,caption:str,delay_ms:int=100)

         sets window width and height and window caption by calling start()

         set delay in ms (default 100) to pause between frames of main loop

        """
        self.start(width,height,caption)
        self.delay_ms = delay_ms

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


    def main_loop(self):
        """
         Runs the main game loop using the delay_ms value.

         Exits correctly when exit is selected.
        """
        self.run = True

        while self.run:
            pygame.time.delay(self.delay_ms)

            #event handler loop here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def stop(self):
        pygame.quit()

def main():
    w = World(800,600,"title") #SVGA : 800x600
    w.main_loop()
    w.stop()

if __name__ == '__main__':
    main()

