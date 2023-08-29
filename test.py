import unittest
from chanda import chanda

class chandrayaanTest(unittest.TestCase):
    def test_initial_position(self):
        chandrayaan = chanda(0, 0, 0, "N")
        self.assertEqual(chandrayaan.x, 0)
        self.assertEqual(chandrayaan.y, 0)
        self.assertEqual(chandrayaan.z, 0)
        self.assertEqual(chandrayaan.direction,"N")
   

    def test_move_forward(self):
        chandrayaan = chanda(0, 0, 0, "N")
        chandrayaan.move_forward()
        self.assertEqual(chandrayaan.y, 1)

    
    def test_move_backward(self):
        chandrayaan = chanda(0, 0, 0, "N")
        chandrayaan.move_backward()
        self.assertEqual(chandrayaan.y, -1)

    def test_turn_left(self):
        chandrayaan = chanda(0, 0, 0, "N")
        chandrayaan.turn_left()
        self.assertEqual(chandrayaan.direction, "W")

    def test_turn_right(self):
        chandrayaan = chanda(0, 0, 0, "N")
        chandrayaan.turn_right()
        self.assertEqual(chandrayaan.direction,"E")
    def test_turn_up_up(self):
        chandrayaan = chanda(0, 0, 0, "U")
        chandrayaan.turn_up()
        self.assertEqual(chandrayaan.direction, "U")

    def test_turn_down_down(self):
        chandrayaan = chanda(0, 0, 0, "D")
        chandrayaan.turn_down()
        self.assertEqual(chandrayaan.direction,"D")

    def test_turn_up_down(self):
        chandrayaan = chanda(0, 0, 0, "D")
        chandrayaan.turn_up()
        self.assertEqual(chandrayaan.direction, "D")

    def test_turn_down_up(self):
        chandrayaan = chanda(0, 0, 0,"U")
        chandrayaan.turn_down()
        self.assertEqual(chandrayaan.direction, "U")



if __name__ == "__main__":
    unittest.main()
