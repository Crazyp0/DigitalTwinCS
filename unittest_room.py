import unittest
from room import Room
from floor import Floor
from room import Direction

class DigitalTestRoom(unittest.TestCase):
    def test_area(self):
        r=Room(100,50,0,0,'bedroom')
        self.assertEqual(r.area(),5000)
        self.assertEqual(r.largeur,50)
        
    def test_room(self):
        f=Floor(300,200,1)
        r=Room(100,50,0,0,'Salon')
        r2=Room(50,50,50,100,'Chambre') 
        r3=Room(300,20,50,0,'couloir')
        r4=Room(50,100,25,125,'test')
        f.addRoom(r)
        f.addRoom(r2)
        f.addRoom(r3)
        f.addRoom(r4)
        names=[]
        for i in f.rooms :
            names.append(i.name)
        self.assertEqual(names,['Salon','Chambre'])
    def test_wall(self):
        f=Floor(300,200,1)
        r=Room(100,50,0,0,'Salon')
        r2=Room(50,50,50,100,'Chambre') 
        r3=Room(300,20,50,0,'couloir')
        r4=Room(50,100,25,125,'test')
        f.addRoom(r)
        f.addRoom(r2)
        f.addRoom(r3)
        f.addRoom(r4)
        r.generateWall()
        r2.generateWall()
        r3.generateWall()
        r4.generateWall()
        for i in f.rooms:
            self.assertEqual(len(i.list_of_wall),4)
    
    def test_door(self):
        f=Floor(300,200,1)
        r=Room(100,50,0,0,'Salon')
        f.addRoom(r)
        r.generateWall()
        r.addDoorOnAWall(25, 15, Direction['NORTH'].value)
        self.assertEqual(len(r.list_of_wall[Direction.NORTH.value].doors),1)
    
    def test_nbpeople(self):
        nbpeople=50
        f=Floor(300,200,1)
        r=Room(100,50,0,0,'Salon')
        r.setNbPeople(nbpeople)
        self.assertEqual(r.nbpeople,nbpeople)
        
        
if __name__ == '__main__':
    unittest.main()