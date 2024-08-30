#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      aho
#
# Created:     28/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
REF BLIT : https://youtu.be/BmLm2vW3SFk
REF MESSAGING : https://youtu.be/hPHWeK4iIkM
"""

from super_globals import *



WIDTH = int()
HEIGHT = int()
WIN = None
BACK = (50,50,50)
FPS = 60


ASSETS = {} # {name : Player()}

PRUNE = list()

MsgEvents = dict()


"""
class Player:

    rect = None
    pos = (0,0)
    size = (0,0)
    MoveEvents = None  # {pygameKey : vector}
    ActEvents = None   # {pygameKey : Method}
    World = None


    def __init__(self,name:str,imageFn:str,x:int=100,y:int=100,speed:float=0.0):
        self.MoveEvents = dict()
        self.ActEvents = dict()
        self.name = name
        self.image = pygame.image.load(os.path.join(ASSETS_PATH,imageFn))
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
"""
"""
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

"""




def setUpRed(ASSETS):

    messages = list()

    P = Player(name="red",imgPath="Assets",imageFn="spaceship_red.png",x=WIDTH//4,y=HEIGHT//2,speed=4.0)
    P.transform((55,40),90)
    P.addMoveEvent(pygame.K_a,(-1,0))
    P.addMoveEvent(pygame.K_d,(1,0))
    P.addMoveEvent(pygame.K_w,(0,-1))
    P.addMoveEvent(pygame.K_s,(0,1))
    P.setWorld(0,0,-6+WIDTH//2,HEIGHT)
    #P.shoot(1)
    #messages.append(lambda : P.shoot(1))

    #P.addActEvent(pygame.K_LCTRL,messages) #>----<<<<<<<



    ASSETS[P.name] = P


    P = None

def setUpYellow(ASSETS):
    messages = list()
    P = None

    P = Player(name="yellow",imgPath="Assets",imageFn="spaceship_yellow.png",x=600,y=HEIGHT//4,speed=4.0)
    P.transform((55,40),-90)
    P.addMoveEvent(pygame.K_LEFT,(-1,0))
    P.addMoveEvent(pygame.K_RIGHT,(1,0))
    P.addMoveEvent(pygame.K_UP,(0,-1))
    P.addMoveEvent(pygame.K_DOWN,(0,1))
    P.setWorld(6+WIDTH//2,0,WIDTH//2-6,HEIGHT)

    #messages.append(lambda:P.shoot(-10,(255,266,0)))
    #P.addActEvent(pygame.K_RCTRL,messages)


    ASSETS[P.name] = P
    P = None

def startGame(w:int,h:int)->None:
    global WIDTH,HEIGHT, WIN, ASSETS, go_right
    WIDTH = w
    HEIGHT = h

    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("twt - pyg in 90 mins!")


    #ASSETS.append(Player("yellow","spaceship_yellow.png",200,200))
    #ASSETS[1].transform((55,40),-90)

def defMsgEvents(MsgEvDict):
    MsgEvDict["BulletOff"] = pygame.USEREVENT + 1
    MsgEvDict["RedHit"] = pygame.USEREVENT + 2
    MsgEvDict["YellowHit"] = pygame.USEREVENT + 3


def drawBoundary(WIN):
    BORDER = (-5+(WIDTH // 2), 0, 10,HEIGHT)
    #print(BORDER)
    BLACK = (0,0,0)
    pygame.draw.rect(WIN,BLACK,BORDER)


def draw_window(WIN):
     WIN.fill(BACK)
     drawBoundary(WIN)

     for name in ASSETS:
        #print("drawing ",name)
        ASSETS[name].draw(WIN)


def handle_moves(event):
    for name in ASSETS:
        ASSETS[name].move(event)

def handle_actions(event):
    if event.type == pygame.KEYDOWN:
        for name in ASSETS:
            ASSETS[name].action(event)


def main_event_loop():
    global PRUNE,num

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    ASSETS["red"].shoot(10,(255,0,0))
##
##                if event.key == pygame.K_RCTRL:
##                    ASSETS["yellow"].shoot(-10,(255,255,0))

            for name in ASSETS:
                if name[:len("bullet-")] == "bullet-":
                    print(ASSETS[name])

            handle_actions(event)

        event = pygame.key.get_pressed()

        handle_moves(event)

        for name in PRUNE:
            ASSETS.pop(name)

        PRUNE = list()

        draw_window(WIN)

        pygame.display.update()

    #endWhile




def main():
    global num
    num = 0
    startGame(900,500)
    setUpRed(ASSETS)
    setUpYellow(ASSETS)
    defMsgEvents(MsgEvents)

    main_event_loop()
    pygame.quit()

if __name__ == '__main__':
    main()
