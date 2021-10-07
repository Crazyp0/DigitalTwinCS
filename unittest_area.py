from room import Room
#from element import Element
import unittest

class DigitalTestArea(unittest.TestCase):
    def test_area(self):
        Bedroom=Room(100,50,0,0)
        self.assertEqual(Bedroom.area(),5000)
        self.assertEqual(Bedroom.largeur,50)
    

if __name__ == '__main__':
    unittest.main()