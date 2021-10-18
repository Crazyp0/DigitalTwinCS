from room import Room
#from element import Element
import unittest
from floor import Floor
from wall import Wall
from room import Direction

class DigitalTestDoor(unittest.TestCase):
    def testDoor(self):
        r=Room(100,50,0,0,'bedroom')
        r.generateWall()
        r.addDoorOnAWall(25, 15, Direction['NORTH'].value)
        self.assertEqual(len(r.list_of_wall[Direction['NORTH'].value].doors),1)
        self.assertEqual(len(r.list_of_wall[Direction['SOUTH'].value].doors),0)
        
if __name__ == '__main__':
    unittest.main()