# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:03:36 2021

@author: matth
"""
from element import Element
from door import Door

class Wall(Element):
    def __init__(self,position,rotation,longueur):
        super().__init__(position,rotation,longueur)
        self.doors=[]
    def addDoor(self,positionOnWall,longueurDoor):
        if(positionOnWall+longueurDoor>self.longueur):
            print("impossible to add the door")
            return
        if(self.rotation==90):
            self.doors.append(Door((self.position[0]+positionOnWall,self.position[1]),self.rotation,longueurDoor))
        elif(self.rotation==0):
            self.doors.append(Door((self.position[0],self.position[1]+positionOnWall),self.rotation,longueurDoor))
        
        
    