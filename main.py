# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:28:38 2021

@author: mrobi
"""
from room import Room
from element import Element
from wall import Wall
import numpy as np
from floor import Floor
from room import Direction
from building import Building
import streamlit as st


from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.models import Label

import pandas as pd

from sklearn.cluster import KMeans

#pip install bokeh==2.2.2



def plotWall(w):
    x0,y0=w.position
    l=w.longueur
    rot=w.rotation #we use direct angles (with trigonometry conventions)
    x1=l*np.cos(rot)+x0   
    y1=l*np.sin(rot)+y0
    p.line([x0, x1], [y0, y1])
   
    
def plotRoom(r):
    list_wall=r.generateWall()
    for i in list_wall:
        plotWall(i)
    citation_x=r.x+r.largeur/2
    citation_y=r.y+r.longueur/2
    citation = Label(x=citation_x, y=citation_y, x_units='data', y_units='data',
                 text=r.name, render_mode='css',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0,text_align='center')
    p.add_layout(citation)
    
def plotFloor(f):
    for r in f.rooms : 
        plotRoom(r)
    plotRoom(Room(f.longueur,f.largeur,0,0,'')) #here we plot the border of the floor

def generatePeople(nb_people,size):
    people=np.random.rand(nb_people,2)
    people[:,0]=people[:,0]*size[0]
    people[:,1]=people[:,1]*size[1]
    return people

def generatePeople2(nb_people,list_floors):
    peoples=pd.DataFrame(columns=['x','y','floor','room'])
    for i in range(len(list_floors)) :
        if i==0 :
            min_index=0
        else :
            min_index=int(sum(nb_people[:i]))
        people_floor=pd.DataFrame(columns=['x','y','floor','room'], index=[i for i in range(min_index,min_index+int(nb_people[i]))])
        size=(list_floors[i].longueur,list_floors[i].largeur)
        samples=np.random.rand(int(nb_people[i]),2)
        people_floor['x'][:]=samples[:,0]*size[1]
        people_floor['y'][:]=samples[:,1]*size[0]
        people_floor['floor'][:]=list_floors[i].floorNb
        peoples=pd.concat([peoples,people_floor])
        for k in list_floors[i].rooms :
            for j in range(len(peoples)):
                if peoples['x'][j]>=k.x and peoples['x'][j]<=k.x+k.largeur and peoples['y'][j]>=k.y and peoples['y'][j]<=k.y+k.longueur : 
                    peoples.at[j,'room']=k.name

    return peoples

def plotDoor(d) :   
    x0,y0=d.position
    l=d.longueur
    rot=d.rotation #we use direct angles (with trigonometry conventions)
    x1=l*np.cos(rot)+x0   
    y1=l*np.sin(rot)+y0
    p.line([x0, x1], [y0, y1],line_width=5, color='red')
    
b=Building()
f=Floor(300,200,1)
b.addOrModifyFloor(f)
f2=Floor(200,200,2)
b.addOrModifyFloor(f2)
r=Room(100,50,0,0,'Salon')
r2=Room(50,50,0,100,'Chambre') 
r3=Room(300,20,50,0,'couloir')
r4=Room(50,100,100,125,'test')
f.addRoom(r)
f.addRoom(r2)
f.addRoom(r3)
f.addRoom(r4)
f2.addRoom(r)
f2.addRoom(r2)
f2.addRoom(r3)
list_floors=[i.floorNb for i in b.floors]
nbPeople=np.zeros(len(list_floors))
option=st.sidebar.selectbox('select floor',list_floors)
for k in range(len(list_floors)):
    nbPeople[k] =st.slider("Number of people in the floor{}".format(k+1), min_value=0,max_value=1000, value=50)


p = figure(plot_width = 600, plot_height = 600, title = 'Map', x_axis_label = 'X', y_axis_label = 'Y')
plotFloor(b.floors[option-1])

r.addDoorOnAWall(25, 15, Direction['NORTH'].value)
plotDoor(r.list_of_wall[Direction['NORTH'].value].doors[0])

people=generatePeople2(nbPeople,b.floors)  
p.circle(x=people[people['floor']==option]['x'],y=people[people['floor']==option]['y'])

st.bokeh_chart(p)

st.sidebar.write("Affluence of people in the floor:")
for i in b.floors[option-1].rooms :
#for i in f.rooms : 
    somme=sum(people[people['floor']==option]['room']==i.name)
    i.setNbPeople(somme)
    st.sidebar.write('{}: {} people'.format(i.name,i.nbpeople))
    
#      somme=0
     
#      for k in people : 
#          if k[0]>=i.x and k[0]<=i.x+i.largeur and k[1]>=i.y and k[1]<=i.y+i.longueur : 
#              somme+=1
             
#      i.setNbPeople(somme)
#      st.sidebar.write('{}: {} people'.format(i.name,i.nbpeople))
    

  
    