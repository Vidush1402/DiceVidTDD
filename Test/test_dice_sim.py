import unittest
import random
from dice_sim import Dice

class TestDiceSim(unittest.TestCase):
    def test_start_game(self):
        dice = Dice()
        n = [1,2,3,4,5,6]
        self.assertTrue(dice.dice_num in n)