# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:01:45 2021

@author: matth
"""
from element import Element
class Door(Element):
    def __init__(self,position,rotation,longueur):
        super().__init__(position,rotation,longueur)