import unittest
import random
from dice_sim import Dice

class TestDiceSim(unittest.TestCase):
    def test_start_game(self):
        dice = Dice()
        dice.start_game()
