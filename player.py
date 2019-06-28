from entity import Entity

class Player(Entity):
    def __init__(self, x, y, char, color, name, blocks=False):
        Entity.__init__(self, x, y, char, color, name, blocks=False)
        self.player_name = "HEMAN"