import random

class Dice():

    def start_game(self):
        dice_num = random.randint(1,6)
        return dice_num

    def play_again(self):
        again = input("Do you want to roll again?")
        if again.lower() == "y":
            return True
        else:
            return False

    def game(self):
        ask_play = input("Do you wanna roll the dice? ")
        if ask_play.lower() == "y":
            bool = True
        else:
            bool = False
        while(bool):
            self.start_game()



