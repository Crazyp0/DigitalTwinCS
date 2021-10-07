# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:39:47 2021

@author: matth
"""
from wall import Wall
import numpy as np

class Room:
    def __init__(self,longueur,largeur,x,y,name):
        self.maxNbCharacter=5
        self.id=0
        self.largeur=largeur
        self.longueur=longueur
        self.x=x
        self.y=y
        if(len(name)>self.maxNbCharacter):
            self.name=name[:15]
        else:
            self.name=name
    
    def generateWall(self):
        list_of_wall=[]
        list_of_wall.append(Wall((self.x,self.y),0,self.largeur))
        list_of_wall.append(Wall((self.x,self.y),np.pi/2,self.longueur))
        list_of_wall.append(Wall((self.x,self.y+self.longueur),0,self.largeur))
        list_of_wall.append(Wall((self.x+self.largeur,self.y+self.longueur),-np.pi/2,self.longueur))
        return list_of_wall
        
    def area(self):
        return self.longueur*self.largeur
        

