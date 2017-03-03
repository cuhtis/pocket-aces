import random
import json

class Card():
    RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    SUITS = ['D','C','H','S']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s-%s" % (self.rank, self.suit)


class Deck():
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        return cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)

    def burn_card(self):
        self.cards.pop(0)

    def __str__(self):
        output = ""
        for card in self.cards:
            output += str(card)
            output += '\n'
        return output


class Player():
    def __init__(self, name, stack):
        pass

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


class Game():
    def __init__(self, players=0):
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        pass

    def play_round(self):
        pass

    def __str__(self):
        pass


def Round():
    def __init__(self, players, dealer):
        self.deck = Deck()
        self.phase = 0
        pass

    def collect_blinds(self):
        pass

    def deal_cards(self):
        pass

    def settle_pot(self):
        pass


def main():
    game = Game()

if __name__ == "__main__":
    main()
