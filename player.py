class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = self.calculate_score(self.hand)

    def draw_card(self, deck):
        card = deck.draw_card()
        return card

    def calculate_score(self, hand):
        score = 0

        for card in hand:
            score += card.value

        return score
