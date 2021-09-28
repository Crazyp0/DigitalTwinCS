# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:39:47 2021

@author: matth
"""

class Room:
    def __init__(self,longueur,largeur,x,y):
        self.id=0
        self.largeur=largeur
        self.longueur=longueur
        self.x=x
        self.y=y
    
    def area(self):
        return self.longueur*self.largeur
        

