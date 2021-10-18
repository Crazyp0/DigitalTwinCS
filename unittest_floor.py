import unittest
from floor import Floor
from room import Room


class DigitalTestFloor(unittest.TestCase):
    def testFloorNb(self):
        f=Floor(300,200,1)
        self.assertEqual(f.floorNb,1)
    def testRoom1(self):
        f=Floor(300,200,1)
        r=Room(200,250,0,0,'room1')
        f.addRoom(r)
        self.assertEqual(len(f.rooms),0)
    def testRoom2(self):
        f=Floor(200,200,1)
        r=Room(50,50,0,0,'room1')
        r2=Room(50,50,25,25,'room2')
        f.addRoom(r)
        f.addRoom(r2)
        self.assertEqual(len(f.rooms),1)
    def testRoom3(self):
        f=Floor(200,200,1)
        r=Room(50,50,0,0,'room1')
        r2=Room(50,50,100,100,'room2')
        r3=Room(70,70,100,100,'room3')
        f.addRoom(r)
        f.addRoom(r2)
        f.addRoom(r3)
        names=[]
        for i in f.rooms:
            names.append(i.name)
        self.assertEqual(names,['room1','room2'])
if __name__ == '__main__':
    unittest.main()