#-------------------------------------------------------------------------------
# Name:        Player.py
# Purpose:     Class Player
#
# Author:      archi
#
# Created:     29/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from super_globals import *

class Player:

    rect = None
    pos = (0,0)
    size = (0,0)
    MoveEvents = None  # {pygameKey : vector}
    ActEvents = None   # {pygameKey : Method}
    World = None


    def __init__(self,name:str,imgPath:str,imageFn:str,x:int=100,y:int=100,speed:float=0.0):
        self.MoveEvents = dict()
        self.ActEvents = dict()
        self.name = name
        self.image = pygame.image.load(os.path.join(imgPath,imageFn))
        self.pos = (x,y)
        self.size = self.image.get_size()
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.speed  = speed

    def draw(self,WIN:pygame.Surface):
        WIN.blit(self.image,self.pos)


    def setWorld(self,topX,topY,width,height):
        self.World = (topX,topY,width,height)

    def addMoveEvent(self,keyEvent,vector:tuple):
        self.MoveEvents[keyEvent] = vector

    def addActEvent(self,keyEvent,callback):
        self.ActEvents[keyEvent] = callback

    def setSpeed(self,speed:float):
        self.speed = speed

    def updateRect(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])

    def transform(self,size:tuple=(55,40),angle:int=0):
        self.image = pygame.transform.scale(self.image,size)

        if angle % 360 != 0:
            self.image = pygame.transform.rotate(self.image,angle)


        self.size = self.image.get_size()
        self.rect = (self.pos[0],self.pos[1],self.size[0],self.size[1])

    def getUnitVector(self,keys_pressed)->tuple:
        vector = (0,0)
        for k in self.MoveEvents:
            #print(k)
            if keys_pressed[k] :
                vector = (
                          vector[0]+self.MoveEvents[k][0],
                          vector[1]+self.MoveEvents[k][1]
                         )

        return vector

    def action(self,event)->tuple:
        if event.type == pygame.KEYDOWN:
            for k in self.ActEvents:
                #print(k)

                if event.key == k :
                    print(self.name," sees ",k)
                    for method in self.ActEvents[k]:
                        method() # run the method



    def move(self,event):
        if self.speed == 0.0:
            return

        vector = self.getUnitVector(event)

        if vector == None or (vector[0]== 0 and vector[1]==0):
            return

        if self.World != None:
            x = self.pos[0] + round(vector[0]*self.speed,0)
            y = self.pos[1] + round(vector[1]*self.speed,0)

            # undo move if invalid
            if (x < self.World[0]) or (x + self.rect[2] > self.World[0]+self.World[2]):
                x = self.pos[0]
            if (y < 0) or (y + self.rect[3] > self.World[1]+self.World[3]):
                y = self.pos[1]

        else:
            x = self.pos[0] + round(vector[0]*self.speed,0)
            y = self.pos[1] + round(vector[1]*self.speed,0)

        self.pos = (x,y)
        self.updateRect()

        #print(self.name,"move to ",self.pos)


    def getImage(self):
        return self.image

    def getPos(self):
        return pos

    def shoot(self,aSpeed,bColour=(255,255,255)):
        bullet = None
        bullet = Bullet(player=self,speed=aSpeed,colour=bColour)
        ASSETS[bullet.name] = bullet
        bullet = None

def main():
    pass

if __name__ == '__main__':
    main()
