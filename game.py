from player import Player
from deck import Deck, Card


class Game():
    def __init__(self, players=0):
        self.players = players
        self.game_round = None

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def play_round(self):
        self.game_round = Round(self.players, 0)

    def __str__(self):
        pass


class Round():
    def __init__(self, players, dealer):
        self.deck = Deck()
        self.phase = 0


    def move_dealer(self):
        pass

    def collect_blinds(self):
        pass

    def deal_cards(self):
        pass

    def settle_pot(self):
        pass
