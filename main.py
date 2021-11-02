# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:28:38 2021

@author: mrobi
"""

from peopleManager import PeopleManager
from uiManager import UiManager
from room import Room
from element import Element
from wall import Wall
from floor import Floor
from room import Direction
from building import Building

from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.models import Label

import numpy as np
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans


#Set up of the building
b=Building()

#Set up of the floors
f=Floor(200,300,1)
b.addOrModifyFloor(f)
f2=Floor(200,300,2)
b.addOrModifyFloor(f2)

#Set up of the rooms
r=Room(100,70,0,0,'Chambre')
r2=Room(100,70,0,100,'bureau') 
r3=Room(200,30,70,0,'couloir')
r4=Room(100,200,100,0,'salon')
r5=Room(50,50,100,100,'Couloir2') 
r6=Room(50,50,100,150,'ascenseur')
r7=Room(100,150,150,100,'cuisine')

r8=Room(200,100,0,0,'Chambre')
r9=Room(150,50,100,0,'hub') 
r10=Room(100,50,150,0,'sas')
r11=Room(50,100,200,0,'chambre2')
r12=Room(50,100,200,50,'chambre3') 
r13=Room(100,150,150,100,'salle de bain')

#Add the rooms on the floors
f.addRoom(r)
f.addRoom(r2)
f.addRoom(r3)
f.addRoom(r4)
f.addRoom(r5)
f.addRoom(r6)
f.addRoom(r7)

f2.addRoom(r8)
f2.addRoom(r9)
f2.addRoom(r10)
f2.addRoom(r11)
f2.addRoom(r12)
f2.addRoom(r13)
f2.addRoom(r6)


list_floors=[i.floorNb for i in b.floors]

#sliders for the graphical interface
nbPeople=np.zeros(len(list_floors))
for k in range(len(list_floors)):
    nbPeople[k] =st.slider("Number of people in the floor{}".format(k+1), min_value=0,max_value=1000, value=200)

plotMng=UiManager(list_floors)
peopleMng=PeopleManager(plotMng) 
plotMng.plotFloor(b.floors[plotMng.getOption()-1])
peopleMng.generatePeople(nbPeople,b.floors)  
peopleMng.calculateCluster(b, plotMng.getOption(), )

plotMng.plot()       

