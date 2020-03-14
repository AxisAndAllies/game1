
class Player:
    def __init__(self, name):
        self.name = name


class Risk:
    def __init__(self):
        self.players = dict()
    
    def add_player(self, name):
        self.players[name] = Player(name)
        print(self.players)
    
    def remove_player(self, name):
        if name in self.players:
            del self.players[name]
        print(self.players)