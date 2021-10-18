# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:41:00 2021

@author: matth
"""
class Building:
    def __init__(self):
        self.floors=[]
        
    def addOrModifyFloor(self,floor,number=None):
        """
        Parameters
        ----------
        floor : Floor
            Floor we want to add on the building.
        number : INT, optional
            If want to add a floor, None. If want to modify an already added floor, number is the number of the floor. The default is None.
        """
        if (number is not None) and (number <len(self.floors)):
            self.floors[number]=floor
        else:
            self.floors.append(floor)
            
        
        