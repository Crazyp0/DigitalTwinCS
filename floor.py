# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:56:26 2021

@author: matth
"""
from room import Room

class Floor:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
        self.rooms=[]
        
    def addRoom(self,room):
        self.rooms.append(room)
    
        