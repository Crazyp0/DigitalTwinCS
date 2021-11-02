
import unittest
from room import Room
from wall import Wall
from room import Direction

class DigitalTestDoor(unittest.TestCase):
    def testDoor(self):
        """
        Test if a door is added
        """
        r=Room(100,50,0,0,'bedroom')
        r.generateWall()
        r.addDoorOnAWall(25, 15, Direction['NORTH'].value)
        self.assertEqual(len(r.list_of_wall[Direction['NORTH'].value].doors),1)
    
    def testDoor2(self):
        """
        Test if the door is added in the correct wall
        """
        r=Room(100,50,0,0,'bedroom')
        r.generateWall()
        r.addDoorOnAWall(25, 15, Direction['NORTH'].value)
        
        self.assertEqual(len(r.list_of_wall[Direction['SOUTH'].value].doors),0)
        
if __name__ == '__main__':
    unittest.main()