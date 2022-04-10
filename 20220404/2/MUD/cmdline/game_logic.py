
"""Implemented game logic."""

import shlex
import cmd
from MUD.create import Monster


class Dungeon(cmd.Cmd):
    """Class that implements a multiplayer dungeon."""

    prompt = '(Dungeon) '
    dungeon_map = [[[] for i in range(10)] for i in range(10)]
    player_pos = (0, 0)

    def do_add(self, args):
        """Use the method, you can navigate the map."""
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon_map[int(x)][int(y)].append(Monster(name, int(hp)))

    def do_show(self):
        """Show cell movement."""
        for x, line in zip(range(10), self.dungeon_map):
            for y, cell in zip(range(10), line):
                for monster in cell:
                    print('{} at ({} {}) hp {}'.format(monster.name, x, y, monster.hp))

    def do_attack(self, args):
        """Make a coordinate attack."""
        monster_name = args
        x, y = self.player_pos
        monsters = self.dungeon_map[x][y]
        for monster in monsters:
            if monster.name == monster_name:
                monster.hp -= 10
                if monster.hp > 0:
                    print('{} lost 10 hp, now has {} hp'.format(monster.name, monster.hp))
                else:
                    print('{} dies'.format(monster.name))
                    monsters.remove(monster)
                break
        else:
            print('no {} here'.format(monster_name))

    def is_pos_valid(self, pos):
        """Validate entered coordinates."""
        return 0 <= pos[0] <= 9 and 0 <= pos[1] <= 9

    def move(self, from_cell, direction):
        """Recognize the movement of the monster."""
        moves = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
        return from_cell[0] + moves[direction][0], from_cell[1] + moves[direction][1]

    def do_move(self, args):
        """Make the monster move."""
        direction = shlex.split(args)[0]
        future_pos = self.move(self.player_pos, direction)
        if self.is_pos_valid(future_pos):
            self.player_pos = future_pos
            x, y = self.player_pos
            print('player at {} {}'.format(x, y))
            if self.dungeon_map[x][y]:
                print('encountered: ' + ', '.join(map(str, self.dungeon_map[x][y])))
        else:
            print('cannot move')

    def complete_attack(self, prefix):
        """End monster attack."""
        x, y = self.player_pos
        monster_names = [monster.name for monster in self.dungeon_map[x][y]]
        return [monster_name for monster_name in monster_names if monster_name.startswith(prefix)]

    def complete_move(self, prefix):
        """End monster move."""
        dirs = ['up', 'down', 'left', 'right']
        return [direction for direction in dirs if direction.startswith(prefix)]
