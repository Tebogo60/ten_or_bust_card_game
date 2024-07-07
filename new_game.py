from player import *


class New_game:

    # for 2 players
    def __init__(self, num_of_players):
        for _ in range(num_of_players):
            player_name = input("Enter name: ")
            players = {}
