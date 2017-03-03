import random


class Card():
    RANKS = [' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10',' J',' Q',' K',' A']
    SUITS = ['d','c','h','s']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "[%s%s]" % (self.rank, self.suit)


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
