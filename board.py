import random

from ..game.card import *


class Board:
    def __init__(self, players, current_player):
        self.deck = self.get_deck()
        self.players = players
        self.current_player = current_player

    @staticmethod
    def get_deck():
        new_deck = []
        suits = ["spades", "clubs", "diamonds", "hearts"]

        for suit in suits:
            for value in range(1, 11):
                if value == 1:
                    new_deck.append(Card(suit, "A"))
                else:
                    new_deck.append(Card(suit, value))

        return new_deck

    @staticmethod
    def shuffle(deck):
        random_deck = []

        for _ in range(len(deck)):
            random_index = random.randint(0, len(deck) - 1)
            random_deck.append(deck[random_index])
            deck.pop(random_index)

        return random_deck
