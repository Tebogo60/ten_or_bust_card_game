class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.card_value(suit, rank)

    def card_value(self, suit, rank):
        if rank == "A" or rank == "2" and suit.lower() == "spades":
            return 1
        elif rank == "10" and suit.lower() == "diamonds":
            return 2
        else:
            return 0
