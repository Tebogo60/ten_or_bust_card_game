# import game_modules
# from ..game.board import Board


def game_options():
    """Returns a list of game options."""

    options = """
 - New game
 - Options
 - Help
 - Exit"""

    return options


def turn_into_list(cmd_list):
    """Returns a list of cmds based on the provided argument."""

    if str(type(cmd_list)) == "<class 'str'>" and " - " not in cmd_list:
        return cmd_list.split(" ")

    elif str(type(cmd_list)) == "<class 'str'>" and " - " in cmd_list:
        return [
            cmd.lower()
            for cmd in cmd_list.replace(" - ", "").split("\n")
            if not cmd == ""
        ]

    elif str(type(cmd_list)) == "<class 'list'>":
        return cmd_list

    else:
        raise ValueError("Invalid Argument!")


def get_input(prompt, valid_cmds):
    """Returns a entered input if in valid commands list (valid_cmds)."""

    enter_cmd = input(prompt)
    while not enter_cmd.lower() in valid_cmds:
        print(f""" *** Invalid input "{enter_cmd}". Please try again. ***""")
        enter_cmd = input(prompt)

    return enter_cmd


def play():
    print(
        f"""Welcome to the game!
Your Options: {game_options()}"""
    )

    get_user_input = get_input(
        """
What would you like to do?
 - """,
        turn_into_list(game_options()),
    )

    print(get_user_input)


if __name__ == "__main__":
    play()
