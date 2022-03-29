"""Start the game when run as package."""

from monster.game_logic import Dungeon

if __name__ == '__main__':
    Dungeon().cmdloop()
