# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:39:47 2021

@author: matth
"""
from enum import Enum
from wall import Wall
import numpy as np

class Direction(Enum):
    SOUTH=0
    WEST=1
    NORTH=2
    EST=3

class Room:
    def __init__(self,longueur,largeur,x,y,name):
        self.maxNbCharacter=15
        self.id=0
        self.largeur=largeur
        self.longueur=longueur
        self.x=x
        self.y=y
        self.listOfWall=[]
        if(len(name)>self.maxNbCharacter):
            self.name=name[:self.maxNbCharacter]
        else:
            self.name=name
    
    def generateWall(self):
        self.list_of_wall.append(Wall((self.x,self.y),0,self.largeur))
        self.list_of_wall.append(Wall((self.x,self.y),np.pi/2,self.longueur))
        self.list_of_wall.append(Wall((self.x,self.y+self.longueur),0,self.largeur))
        self.list_of_wall.append(Wall((self.x+self.largeur,self.y+self.longueur),-np.pi/2,self.longueur))
        return self.list_of_wall
    
    def addDoorOnAWall(self,positionOnWall,longueurDoor,direction):
        if(self.listOfWall[direction]!=None):
            self.listOfWall[direction].addDoorOnAWall(positionOnWall,longueurDoor)
          
    def area(self):
        return self.longueur*self.largeur
        

