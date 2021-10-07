from room import Room
#from element import Element
import unittest
from floor import Floor

class DigitalTestRoom(unittest.TestCase):
    def test_room(self):
        f=Floor(300,200)
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
    

if __name__ == '__main__':
    unittest.main()