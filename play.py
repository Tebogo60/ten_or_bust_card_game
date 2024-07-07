from board import *
from player import *


class Game:
    def __init__(self):
        self.board = Board()

    def get_input(self, prompt, input_type):
        print(prompt)
        user_input = input(" - ")

        while not (
            user_input
            or user_input.isdigit()
            and input_type == "integer"
            or user_input.isdigit()
            and input_type == "string"
        ):
            print(f"Invalid input '{user_input}', expect '{input_type}'!\n")

            print(prompt)
            user_input = input(" - ")

        return user_input

    def create_players(self, number_of_players):
        for _ in range(int(number_of_players)):
            get_player_name = self.get_input("Enter your name:")
            self.board.add_player(Player(get_player_name))

    def play(self):
        number_of_players = self.get_input("Enter number of players:")
        self.create_players(number_of_players)
