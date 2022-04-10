
"""It's a file that contains all game entities."""


class Monster:
    """Simple monster class. Every moster has name and HP."""

    def __init__(self, name, hp):
        """Initialize."""
        self.name = name
        self.hp = hp

    def __str__(self):
        """Display the name of the hero and his HP in a string."""
        return '{} {} hp'.format(self.name, self.hp)
