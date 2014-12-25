"""Exercise 47 - Learning Python the Hard Way"""


class Room(object):
    """The room will be testing..."""

    def __init__(self, name, description):
        """Initialise the room"""
        self.name = name
        self.description = description
        self.paths = {}

    def gamego(self, direction):
        """Start the game"""
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """Add the relevant paths"""
        self.paths.update(paths)
