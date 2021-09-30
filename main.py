# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:28:38 2021

@author: mrobi
"""
from room import Room
from element import Element
from wall import Wall
import numpy as np

import matplotlib.lines as lines
import matplotlib.pyplot as plt



def plotWall(w,fig):
    x0,y0=w.position
    l=w.longueur
    rot=w.rotation #we use direct angles (with trigonometry conventions)
    x1=l*np.cos(rot)+x0   
    y1=l*np.sin(rot)+x1
    line = lines.Line2D([x0, x1], [y0, y1], transform=fig.transFigure, figure=fig)
    fig.lines.extend([line])
    return fig
    
    
def plotRoom(r,fig):
    list_wall=r.generateWall()
    for i in list_wall:
        plotWall(i,fig)
    
fig=plt.figure() #a mettre plus tard dans plotFloor ou plotArea   
r=Room(100,50,0,0)
fig=plotRoom(r,fig) 
plt.show()
    
    
    
    
    