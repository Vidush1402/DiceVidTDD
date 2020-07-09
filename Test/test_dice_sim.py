import unittest


class Dice():

    def start_game(self):
        return "Press start"


class TestDiceSim(unittest.TestCase):
    def test_start_game(self):
        dice = Dice()
        self.assertEqual(dice.start_game(), "Press start")