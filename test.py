import unittest
from chanda import chanda, NORTH

class chandrayaanTest(unittest.TestCase):
    def test_initial_position(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        self.assertEqual(chandrayaan.x, 0)
        self.assertEqual(chandrayaan.y, 0)
        self.assertEqual(chandrayaan.z, 0)
        self.assertEqual(chandrayaan.direction, NORTH)
    


if __name__ == "__main__":
    unittest.main()
