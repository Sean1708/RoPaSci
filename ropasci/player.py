import random

from getpass import getpass


class Player:

    def __init__(self, game, name=None):
        self.game = game
        self.name = name
        self.wins = 0
        self.choices = []

    def choose(self):
        choice = getpass("{0}, make a choice: ".format(self.name)).lower()
        while True:
            if choice in self.game.plays.keys():
                self.choices.append(choice)
                break
            else:
                choice = getpass("Invalid choice. Choose again: ")

class Computer(Player):

    def choose(self):
        print("{0} is choosing...".format(self.name))
        choice = random.choice(list(self.game.plays.keys()))
        self.choices.append(choice)
