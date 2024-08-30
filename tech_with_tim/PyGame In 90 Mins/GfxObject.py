#-------------------------------------------------------------------------------
# Name:        GfxObject.py
# Purpose:     Class Player
#
# Author:      archi
#
# Created:     29/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from super_globals import *

class GfxObject:
    name = None
    rect = None
    image = None
    pygameDraw = None

    def __init__(self,name:str,posX:int=0,posY:int=0,speed:float):
        self.name = name
        self.rect = pygame.Rect(posX,posY,0,0) #width and height defaults 0,0
        self.drawError = 0
        self.size = self.image.get_size()
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.speed  = speed

    def setImage(self,imgPath:str,imageFn:str):
        try:
            self.image = pygame.image.load(os.path.join(imgPath,imageFn))
        except:
            this.image = None
            print(f"this = {self.name} WARNING! ----------------------------")
            print("   this.setImage(imgPath={},imageFn={}) failed!         ")
            print("   this.image --> None                                  ")
            print("--------------------------------------------------------")
        else:
            size = self.image.get_size()
            self.rect = pygame.Rect(self.rect.x,self.rect.y,size[0],size[1])

    def setPygameDraw(self,pygameDraw=None):
        """
         def drawMe(WIN)-> pygame.Rect :

         paramterless function that uses pygame.draw
         parameter of the surface window WIN must be supplied
         returns a pygame.Rect containing the "drawn"" image
        """
        if pygameDraw == None or not isfunction(pygameDraw):
            print(f"this = {self.name} WARNING! ----------------------------")
            print(f"   this.setPygameDraw(pygameDraw={pygameDraw}) failed!  ")
            print("    this.pygameDraw --> None                            ")
            print("--------------------------------------------------------")
        self.pygameDraw = pygameDraw


    def draw(self,WIN:pygame.Surface):
        self.drawError = 0
        if hasattr(self,'image') and self.image != None:
            WIN.blit(self.image,self.rect)
        elif hasattr(self,'pygameDraw') and self.pygameDraw != None:
            self.pygameDraw(WIN)
        else:
            self.drawError += 1

        if 0<self.drawError and self.drawError < 3:
            print(f"{self.name} WARNING! ----------------------------------")
            print("  > No image - please set with .setImage(path,filename)")
            print("  > No pygameDraw method. Set with setPygameDraw:      ")
            print("   +--> Requires a function f(WIN).                    ")
            print("-------------------------------------------------------")

    def updateRect(self):
        if self.image != None:
            self.size = self.image.get_size()
            self.rect = (self.pos[0],self.pos[1],self.size[0],self.size[1])


    def transformImage(self,size:tuple=(55,40),angle:int=0):
        if self.image == None:
            return

        self.image = pygame.transform.scale(self.image,size)

        if angle % 360 != 0:
            self.image = pygame.transform.rotate(self.image,angle)

        self.updateRect()



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



def main():


if __name__ == '__main__':
    main()
