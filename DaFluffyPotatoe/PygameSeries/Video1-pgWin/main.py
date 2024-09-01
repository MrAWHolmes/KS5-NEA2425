"""
main.py
"""

import pygame
import sys

class World:
    
    def __init__(self,width:int,height:int,fps:int=60):
        self.rect = pygame.Rect(0,0,width,height)
        self.fps = fps
    
    def initWindow(self):
        self.WIN = pygame.display.set_mode((self.rect.width,self.rect.height))


        