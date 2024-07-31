#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Main game loop, driver
#
# Author:      Mr Holmes
#
# Created:     28-07-2024
# Copyright:   (c) DaVader 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# REF: https://youtu.be/B6DrRN5z_uU (Tech with Tim)

#-------------------------------------------------------------------------------
import os
import random
import math
import pygame

#for dynamic file loading
from os import listdir
from os.path import isfile, join

#load Player class
from player import Player,SpritePlayer

#globals
BG_COLOR = (255,255,255)


class Screen:
    #screen
    bg_color = tuple()
    caption :str = "caption"
    width : int = 500
    height : int = 500
    window = None       #pygame window
    clock : None
    running: bool = True

    #background
    bg_tilePos = list()
    bg_image = None

    #frames per second - static set here
    fps : int = 60

    #contained class objects
    objects  : None
    moveable : None

    def __init__(self,captionStr:str,width:int,height:int,bg_color:tuple):
        self.width = width
        self.height = height
        self.caption = captionStr
        self.bg_color = bg_color

        #initialise pygame
        pygame.init()
        pygame.display.set_caption(self.caption)
        size = (self.width,self.height)
        self.window = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.objects = {} #empty dictionary
        self.moveable = {} # {'key':[boolMove,floatGravity]}


    def addObject(self,theObject,moveable=False):
        self.objects[theObject.id] = theObject
        self.moveable[theObject.id]=[moveable,theObject.grav]

    def popObject(self,objectId):
        """
         Removes Object with ObjectId from the objects dictionary
        """
        popObject = self.objects[objectId]
        self.objects.pop(objectId)
        del popObject

    #ref: https://stackoverflow.com/questions/7580532/how-to-check-whether-a-method-exists-in-python
    def has_method(self,obj,method)->bool:
        return callable(getattr(obj,method,None))



    def loadBackground(self,name):
        """
          name : str - name of background image in ./assets/Background/ folder

          sets:
            self.bg_tile
        """
        try:
            fullName = join("assets","Background",str(name))
            self.bg_image = pygame.image.load(fullName)
        except:
            print("Error! Cannot load bg_file : ", fullName)
            self.bg_image = None
            self.bg_tilePos = []
        else:
            print(f"background {fullName} loaded...")
            _, _, width, height = self.bg_image.get_rect()

            # loop to render background
            # note use of div!
            for x in range(1 + self.width // width):
                for y in range(1 + self.height // height):
                    pos = (x*width,y*height)
                    self.bg_tilePos.append(pos)

    def drawBackground(self):
        for pos in self.bg_tilePos:
            self.window.blit(self.bg_image,pos)


    def draw(self):
        for key in self.objects:
            #print(f"drawing {key} ...")
            self.objects[key].draw(self.window)

    def loop(self):
        killList = []
        for key in self.objects:
            if self.moveable[key][0]:
                self.objects[key].loop()

            if self.moveable[key][1] != 0.0:
                self.objects[key].gravity(self.fps)

            #check if destroyed - add it to the kill list
            if self.has_method(self.objects[key],"checkAlive"):
                if not self.objects[key].checkAlive():
                    killList.append(key)

        #process kill list
        for key in killList:
            if key == "GreenPlayer":
                self.popObject(key)
                print(f"object {key} was destroyed")
                return False
            else:
                self.popObject(key)
                print(f"object {key} was destroyed")

        return True



    def mainLoop(self):
        while self.running:
            self.clock.tick(self.fps)

            #handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            #update display
            self.drawBackground()

            self.running = self.loop()

            #call contained objects draw method
            self.draw()

            #redraw display window
            pygame.display.update()




    def quit(self):
        if self.running == False:
            pygame.quit()
            quit(0)






def main():
    global World
    World = Screen("Tech with Tim Platformer",1000,800,BG_COLOR)
    World.loadBackground("Blue.png")

    GreenPlayer = Player("GreenPlayer",Player.GREEN)
    GreenPlayer.bindKeys(pygame.K_a,pygame.K_d,pygame.K_SPACE)
    World.addObject(GreenPlayer,True)

    RedPlayer = Player("RedPlayer",Player.RED,3)
    RedPlayer.bindKeys(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_RETURN)
    World.addObject(RedPlayer,True)



    World.mainLoop()

    World.quit()


if __name__ == '__main__':
    main()
