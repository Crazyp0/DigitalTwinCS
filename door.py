# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:01:45 2021

@author: matth
"""
from element import Element
class Door(Element):
    def __init__(self,position,rotation,longueur):
        """
        Parameters
        ----------
        position : [INT, INT]
            The first element of the tuple is the position of the door along the x axis, and the second is along the y axis.
        rotation : INT
            Must be 0, np.pi/2 or -np.pi/2, depending on the orientation of the door (horizontal, or vertical).
        longueur : INT
            Length of the door.
        """
        super().__init__(position,rotation,longueur)