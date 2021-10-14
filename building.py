# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:41:00 2021

@author: matth
"""
class Building:
    def __init__(self):
        self.floors=[]
        
    def addOrModifyFloor(self,floor,numero=None):
        if (numero is not None) and (numero <len(self.floors)):
            self.floors[numero]=floor
        else:
            self.floors.append(floor)
            
        
        