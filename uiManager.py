# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:22:56 2021

@author: matth
"""
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.models import Label
from room import Room
import streamlit as st

class UiManager:
    def __init__(self,list_floors):
        st.sidebar.write("Affluence of people in the floor:")
        self.fig=figure(plot_width = 600, plot_height = 600, title = 'Map', x_axis_label = 'X', y_axis_label = 'Y')
        self.list_floors=list_floors
        self.option=st.sidebar.selectbox('select floor',self.list_floors)
        
    def getOption(self):
        return self.option
    
    def plotWall(self,w):
        x0,y0=w.position
        l=w.longueur
        rot=w.rotation #we use direct angles (with trigonometry conventions)
        x1=l*np.cos(rot)+x0   
        y1=l*np.sin(rot)+y0
        self.fig.line([x0, x1], [y0, y1])
       
        
    def plotRoom(self,r):
        list_wall=r.generateWall()
        for i in list_wall:
            self.plotWall(i)
        citation_x=r.x+r.largeur/2
        citation_y=r.y+r.longueur/2
        citation = Label(x=citation_x, y=citation_y, x_units='data', y_units='data',
                     text=r.name, render_mode='css',
                     border_line_color='black', border_line_alpha=1.0,
                     background_fill_color='white', background_fill_alpha=1.0,text_align='center')
        self.fig.add_layout(citation)
        
    def plotFloor(self,f):
        for r in f.rooms : 
            self.plotRoom(r)
        self.plotRoom(Room(f.longueur,f.largeur,0,0,'')) #here we plot the border of the floor
        
    def plotDoor(self,d) :   
        x0,y0=d.position
        l=d.longueur
        rot=d.rotation #we use direct angles (with trigonometry conventions)
        x1=l*np.cos(rot)+x0   
        y1=l*np.sin(rot)+y0
        self.fig.line([x0, x1], [y0, y1],line_width=5, color='red')
    
    def drawCircle(self,a,b,c):
        self.fig.circle(x=a,y=b,color=c)
    
    def displayRoomInfo(self,name,number):
        st.sidebar.write('{}: {} people'.format(name,number))
    
    def plot(self):
        st.bokeh_chart(self.fig)