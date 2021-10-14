# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:56:26 2021

@author: matth
"""
from room import Room

class Floor:
    def __init__(self,longueur,largeur,num):
        self.longueur=longueur
        self.largeur=largeur
        self.rooms=[]
        self.floorNb=num
        
    def addRoom(self,room):
        if(room.x+room.largeur>self.largeur or room.y+room.longueur>self.longueur):
            print("room too large")
            return
        for r in self.rooms:
            if((room.x>=r.x+r.largeur or room.x+room.largeur<=r.x or room.y>=r.y+r.longueur or room.y+room.longueur<=r.y)==False):
                print("impossible to add this room")
                return
        self.rooms.append(room)
    
        