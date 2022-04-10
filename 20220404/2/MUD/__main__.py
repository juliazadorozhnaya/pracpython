"""Start the game when run as package."""

from MUD.cmdline.game_logic import Dungeon


if __name__ == '__main__':
    Dungeon().cmdloop()
