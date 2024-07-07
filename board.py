from deck import Deck


class Board:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.community_cards = []

    def add_player(self, player):
        self.players.append(player)

    def check_winner(self):
        winner = max([player.score for player in self.players])
        return winner
