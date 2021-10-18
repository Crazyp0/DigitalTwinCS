import unittest
from floor import Floor
from building import Building

class DigitalTestBuilding(unittest.TestCase):
    def testAddFloor(self):
        b=Building()
        f=Floor(300,200,1)
        b.addOrModifyFloor(f)
        self.assertEqual(len(b.floors),1)
    def testModifyFloor(self):
        b=Building()
        f=Floor(300,200,1)
        b.addOrModifyFloor(f)
        f=Floor(300,200,1)
        b.addOrModifyFloor(f,0)
        self.assertEqual(len(b.floors),1)
    def testModifyFloor2(self):
        b=Building()
        f=Floor(300,200,1)
        b.addOrModifyFloor(f)
        f=Floor(200,200,1)
        b.addOrModifyFloor(f,0)
        self.assertEqual(b.floors[0].longueur,200)
    
if __name__ == '__main__':
    unittest.main()