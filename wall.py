# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:03:36 2021

@author: matth
"""
from element import Element
from door import Door
import numpy as np

class Wall(Element):
    def __init__(self,position,rotation,longueur):
        """
        Parameters
        ----------
        position : [INT,INT]
            the first argument is the position of the wall on the x axis, and the second on the y axis.
        rotation : INT
            must be equal to : 0, np.pi/2 or -np.pi/2, depending if the wall is horizontal or vertical.
        longueur : INT
            Length of the wall.
        """
        super().__init__(position,rotation,longueur)
        self.doors=[]
        
    def addDoor(self,positionOnWall,longueurDoor):
        """
        Parameters
        ----------
        positionOnWall : INT
            position of the door on the wall. Must be smaller than the length of the wall.
        longueurDoor : INT
            length of the door. Must be smaller than the length of the wall.
        """
        if(positionOnWall+longueurDoor/2>self.longueur or positionOnWall-longueurDoor/2<0):
            print('impossible to add Door')
            return
        if self.rotation==np.pi/2:
            self.doors.append(Door((self.position[0],self.position[1]+positionOnWall-longueurDoor/2),self.rotation,longueurDoor))
        elif self.rotation==-np.pi/2:
            self.doors.append(Door((self.position[0],self.position[1]-positionOnWall+longueurDoor/2),self.rotation,longueurDoor))
        elif self.rotation==0 :
            self.doors.append(Door((self.position[0]+positionOnWall-longueurDoor/2,self.position[1]),self.rotation,longueurDoor))
        
        
    