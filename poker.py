import random

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

    def print_deck(self):
        for card in self.cards:
            print(card)


def main():
    deck = Deck()
    deck.print_deck()

main()
