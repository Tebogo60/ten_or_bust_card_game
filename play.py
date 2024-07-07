from board import *
from player import *


class Game:
    player_names = []

    def __init__(self):
        self.board = Board()

    def get_input(self, prompt, input_type):
        print(prompt)
        user_input = input(" - ")

        while (
            not user_input
            or not user_input.isdigit()
            and input_type == "integer"
            or not user_input.isalpha()
            and input_type == "string"
        ):
            print(f"\n >>> Invalid input '{user_input}', expect '{input_type}'! <<<\n")

            print(prompt)
            user_input = input(" - ")

        return user_input

    def add_players(self, number_of_players):
        for i in range(int(number_of_players)):
            while True:
                get_player_name = self.get_input(
                    f"\nPlayer No.{i+1}, enter your name:", "string"
                )

                if not get_player_name in self.player_names:
                    self.player_names.append(get_player_name)
                    break
                else:
                    print("\n >>> Name taken, pick another name. <<<\n")

            self.board.add_player(Player(get_player_name))

    def play(self):
        number_of_players = self.get_input("Enter number of players:", "integer")
        self.add_players(number_of_players)
        self.board.deck.shuffle()

        current_player_idx = 0
        while True:
            community_cards = []

            try:
                current_player = self.player_names[current_player_idx]
            except IndexError:
                current_player_idx = 0
                current_player = self.player_names[current_player_idx]

            top_card = self.board.deck.draw_card().get_card()
            print(
                f"\n{current_player[0].upper() + current_player[1:]} you picked {top_card}"
            )

            user_input = self.get_input("What do you want to do?", "string")

            break


if __name__ == "__main__":
    # Initialize the Game instance
    start_game = Game()

    # Start the game by calling the play() method
    start_game.play()
