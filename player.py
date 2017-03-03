from enum import Enum


class Player():
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack
        self.cards = None
        self.state = self.State.FOLDED

    def __str__(self):
        pass

    def fold(self):
        pass

    def check(self):
        pass

    def call(self):
        pass

    def raisebet(self, amount):
        pass

    def stack_gain(self, amount):
        pass

    def stack_loss(self, amount):
        pass

    class State(Enum):
        OBSERVING = "observing"
        PLAYING = "playing"
        FOLDED = "folded"
