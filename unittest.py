from room import Room
import unittest

class RoomTest(unittest.TestCase):
    def test_area(self):
        Bedroom=Room(100,50,0,0)
        self.assertEqual(Bedroom.area(),5000)

if __name__ == '__main__':
    unittest.main()