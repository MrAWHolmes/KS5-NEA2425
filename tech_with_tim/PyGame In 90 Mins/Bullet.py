#-------------------------------------------------------------------------------
# Name:        Bullet.py
# Purpose:
#
# Author:      archi
#
# Created:     29/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from super_globals import *

class Bullet:
    count = 0
    rect = None
    pos = (0,0)
    size = (0,0)
    World = None
    colour = None
    owner = None


    def __init__(self,player:Player,speed,colour=(255,0,0)):
        self.rect = pygame.Rect(player.pos[0]+player.rect[2]//2,
                                 player.pos[1]+player.rect[3]//2,
                                 10,10)
        self.size = (self.rect[2],self.rect[3])
        self.colour = colour

        if Bullet.count > 100:
            Bullet.count = 0

        Bullet.count +=1
        self.MoveEvents = dict()
        self.ActEvents = dict()
        self.name = "bullet-"+player.name+str(Bullet.count)
        self.speed  = speed
        self.owner = player.name

    def __str__(self):
        return self.name + f": ({self.rect[0]},{self.rect[1]})"

    def draw(self,WIN:pygame.Surface):
        self.updateRect()
        print(self.rect)
        pygame.draw.rect(WIN,self.colour,self.rect)

    def updateRect(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])

    def move(self,keys_pressed):

        global PRUNE
        vector = (1,0)
        bulletOff = False
        x = self.rect[0] + round(vector[0]*self.speed,0)
        y = self.rect[1]

        if self.speed < 0:
            #moving left
            if x < 5:
                bulletOff = True

        else: #moving right
            if x - self.rect[2] > WIDTH-5:
                bulletOff = True

        if bulletOff:
            PRUNE.append(self.name)
            return

        self.pos = (x,y)
        self.updateRect()

        #print(self.name,"move to ",self.pos)

    def action(self,event):
        pass

    def check_hit(self,Enemy:Player):

        if self.rect.colliderect(Enemy.rect):
            if self.owner == "red":
                hitMsg = "YellowHit"
            else:
                hitMsg = "RedHit"

            pygame.event.post(pygame.event.Event(MsgEvents[hitMsg]))
            ASSETS.pop(self.name)




def main():
    pass

if __name__ == '__main__':
    main()
