#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:
#
# Author:     Mr Holmes
#
# Created:     28-07-2024
# Copyright:   (c) DaVader 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
#for dynamic file loading
from os import listdir
from os.path import isfile, join

class Player(pygame.sprite.Sprite):
    #Colour CONSTS
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    #id
    id = ""

    #velocity/direction
    max_vel   : int = 0
    x_vel     : int = 0
    y_vel     : int = 0
    grav      : float = 0.0
    fallCount : int = 0

    #rect
    rect = None
    mask = None

    #image/animation
    direction=""
    anim_count = 0
    colour = None

    #keys
    leftK = None
    rightK = None
    upK = None
    downK = None
    useK = None

    #status:
    alive : bool = True





    def __init__(self,nameStr:str,color:tuple=(255,255,255),width=32,height=32,max_vel=5,gravity=1.0):
        """
         nameStr : Index String for injection into World using World.addObject(str,Oject)
         rect_dim=(x:int,y:int,width:int,height:int)
        """



        #set index String so its not null
        if nameStr == "":
            nameStr = "player"
        self.id = str(nameStr)




        self.rect.COPY(rect_dim)
        self.colour = color

        self.direction = "left"

        #set velocities
        self.max_vel = max_vel
        self.grav = gravity

    def bindKeys(self,leftK=None,rightK=None,jumpK=None,fireK=None,upK=None,downK=None,useK=None):
        """
         binkKeys(leftK=None,rightK=None,jumpK=None,fireK=None,upK=None,downK=None,useK=None)
        """
        self.leftK = leftK
        self.rightK = rightK
        self.upK = upK
        self.downK = downK
        self.useK = useK
        self.jumpK=jumpK
        self.fireK=fireK


    def name(self):
        return self.nameStr


    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self,vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.anim_count = 0


    def move_right(self,vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.anim_count = 0

    def handleMove(self):
        keys = pygame.key.get_pressed()

        #set my x-velocity to 0 and change with key press
        self.x_vel = 0

        if self.leftK != None and keys[self.leftK]: #left
            self.move_left(self.max_vel)

        if self.rightK != None and keys[self.rightK]:#right
            self.move_right(self.max_vel)

    def loop(self):
        self.handleMove()
        self.move(self.x_vel,self.y_vel)

    def checkAlive(self):
        return self.alive

    def gravity(self,fps):
        self.y_vel += min(self.grav,(self.fallCount/fps)*self.grav)
        self.fallCount += 1

        if self.fallCount > 200: #are we dead???
            self.fallCount = 0
            self.alive = False



    def draw(self,win):
        """
            win must be the Screen Windows of the main pygame app
        """
        pygame.draw.rect(win,self.colour,self.rect)

class SpritePlayer(Player):
    all_sprites = None

    def __init__(self,pathDir,nameStr:str,rect_dim:tuple=(0,0,32,32),max_vel=5,gravity=1.0):
        super().__init__(nameStr,rect_dim,(255,255,255),max_vel,gravity)


        self.all_sprites = self.load_sprite_sheets(pathDir,32,32)

    def flip(self,sprites):
        return [pygame.transform.flip(aSprite,True,False) for aSprite in sprites]

    def load_sprite_sheets(self,spritePath,width,height,direction=False):

        images = [f for f in listdir(spritePath) if isfile(join(path,f))]

        self.all_sprites = {}

        for image in images:
            spriteSheet = pygame.image.load(join(path,image)).convert_alpha()

            sprites = []                             # rect2(x,y,width,heigth)
            for i in range(spriteSheet.get_width()//width):
                surface = pygame.surface((width,height),pygame.SRCALPHA,32)
                rect = pygame.Rect(i*width,0,width,height)
                surface.blit(spriteSheet,(0,0),rect)
                sprites.append(pygame.transform.scale2x(surface))

            if direction:
                self.all_sprites[image.replace(".png","")+"_right"] = sprites
                self.all_sprites[image.replace(".png","")+"_left"] = self.flip(sprites)
            else:
                 self.all_sprites[image.replace(".png","")] = sprites


    def draw(self,win):
        self.sprite = self.all_sprites["idle"][0]
        win.blit(self.sprite,(self.rect.x,self.rect.y))





def main():
    print("Nothing to do in Player.py .. run from main.py")

if __name__ == "__main__":
    main()
