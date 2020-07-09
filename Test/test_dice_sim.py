import unittest


class Dice(object):
    pass


class TestDiceSim(unittest.TestCase):
    def test_start_game(self):
        dice = Dice([])
        self.assertEqual(dice.start_total(), "Press start")