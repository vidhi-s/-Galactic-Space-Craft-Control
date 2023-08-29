import unittest
from chanda import chanda, NORTH

class chandrayaanTest(unittest.TestCase):
    def test_initial_position(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        self.assertEqual(chandrayaan.x, 0)
        self.assertEqual(chandrayaan.y, 0)
        self.assertEqual(chandrayaan.z, 0)
        self.assertEqual(chandrayaan.direction, NORTH)
   

    def test_move_forward(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        chandrayaan.move_forward()
        self.assertEqual(chandrayaan.y, 1)

    
    def test_move_backward(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        chandrayaan.move_backward()
        self.assertEqual(chandrayaan.y, -1)

    def test_turn_left(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        chandrayaan.turn_left()
        self.assertEqual(chandrayaan.direction, "W")

    def test_turn_right(self):
        chandrayaan = chanda(0, 0, 0, NORTH)
        chandrayaan.turn_right()
        self.assertEqual(chandrayaan.direction,"E")



if __name__ == "__main__":
    unittest.main()
