# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:36:44 2021

@author: matth
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

class PeopleManager:
    
    def __init__(self,uiMng):
        self.colors=['red','blue','yellow']
        self.uiMng=uiMng
    
    def generatePeople(self,nb_people,list_floors):
        """
        Parameters
        ----------
        nb_people : Array 
            Array containing the number of people that are on each floor.
        list_floors : Array
            Array containing each floor.

        Returns
        -------
        None.
        Generate random people in the floors, and calculate in each room they are.

        """
        self.peoples=pd.DataFrame(columns=['x','y','floor','room'])
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
            for k in list_floors[i].rooms :
                for j in range(min_index,min_index+int(nb_people[i])):
                    if people_floor['x'][j]>=k.x and people_floor['x'][j]<=k.x+k.largeur and people_floor['y'][j]>=k.y and people_floor['y'][j]<=k.y+k.longueur : 
                        people_floor.at[j,'room']=k.name
            self.peoples=pd.concat([self.peoples,people_floor])
    
    def calculateCluster(self,b,option):
        """
        

        Parameters
        ----------
        b : Building
            Building containing all the floors.
        option : INT
            Integer representing the floor that is selected.

        Returns
        -------
        None.
        Calculate the 3 clusters that are in each room of the floor and plot them in different colors

        """
        people_floor=self.peoples[self.peoples['floor']==option]
        for i in b.floors[option-1].rooms :
            somme=sum(people_floor['room']==i.name)
            i.setNbPeople(somme)
            self.uiMng.displayRoomInfo(i.name,i.nbpeople)
            if somme>2: 
                clusters=3
            else :
                clusters=somme
            kmeans = KMeans(n_clusters=clusters, random_state=0)
            people_room=people_floor[people_floor['room']==i.name]
            if len(people_room)>0:
                kmeans.fit(people_room[['x','y']])
                
                people_clustered=people_room.copy()
                people_clustered['cluster']=kmeans.labels_
                for k in range(clusters):
                    self.uiMng.drawCircle(people_clustered[people_clustered['cluster']==k]['x'],people_clustered[people_clustered['cluster']==k]['y'],self.colors[k])