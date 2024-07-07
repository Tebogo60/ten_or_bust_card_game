class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.score = 0

    def update_score(self, points):
        self.score += points

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(cards)
