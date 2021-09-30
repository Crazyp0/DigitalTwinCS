# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:03:36 2021

@author: matth
"""
from element import Element

class Wall(Element):
    def __init__(self,position,rotation,longueur):
        super().__init__(position,rotation,longueur)
    