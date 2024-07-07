from board import *


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

    def play(self):
        number_of_players = self.get_input("Enter number of players")
