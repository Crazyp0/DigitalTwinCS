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
    def __init__(self,longueur,largeur,x,y,name,*nbpeople):
        """
        Parameters
        ----------
        longueur : INT
            length of the room, along the y axis.
        largeur : INT
            width of the room, along the x axis.
        x : INT
            position along the axis x of the bottom-left-hand corner of the room.
        y : INT
            position along the axis y of the bottom-left-hand corner of the room.
        name : STR
            name of the room.
        *nbpeople : INT
            number of people in the room.
        """
        
        self.maxNbCharacter=15
        self.id=0
        self.largeur=largeur
        self.longueur=longueur
        self.x=x
        self.y=y
        self.list_of_wall=[]
        self.nbpeople=0
        if(len(name)>self.maxNbCharacter):
            self.name=name[:self.maxNbCharacter]
        else:
            self.name=name
    
    def generateWall(self):
        """
        Returns
        -------
        list_of_wall
            list with the 4 walls of the room.
        """
        self.list_of_wall.append(Wall((self.x,self.y),0,self.largeur))
        self.list_of_wall.append(Wall((self.x,self.y),np.pi/2,self.longueur))
        self.list_of_wall.append(Wall((self.x,self.y+self.longueur),0,self.largeur))
        self.list_of_wall.append(Wall((self.x+self.largeur,self.y+self.longueur),-np.pi/2,self.longueur))
        return self.list_of_wall
    
    def addDoorOnAWall(self,positionOnWall,longueurDoor,direction):
        """
        Parameters
        ----------
        positionOnWall : INT
            Position where the door is on the wall.
        longueurDoor : INT
            Length of the door.
        direction : INT
            Can use Direction['NORTH'].value if want to display the door on the north wall.
        """
        if(self.list_of_wall[direction]!=None):
            self.list_of_wall[direction].addDoor(positionOnWall,longueurDoor)
            
          
    def area(self):
        """
        Returns
        -------
        INT
            Area of the room.
        """
        return self.longueur*self.largeur
    
    def setNbPeople(self, nbpeople):
        """
        Parameters
        ----------
        nbpeople : INT
            number of people in the room.
        """
        self.nbpeople=nbpeople

