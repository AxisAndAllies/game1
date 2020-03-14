class Game:
    nodes = {
        1: [2,3],
        2:[1,3],
        3: [1,2]
    }

    players = ['a','b']

    pieces = {
        1: {
            "player_index": 0,
            "strength": 22
        },
        2: {
            "player_index": 0,
            "strength": 30
        },
        3: {
            "player_index": 1,
            "strength": 25
        }
    }



    def move(self, num, node_index_from, node_index_to):
        player_index = self.cur_player
        self._check_valid_node(node_index_from)
        self._check_valid_node(node_index_to)
        self._check_player_owns(player_index, node_index_from)
        if 
        to_owner = self.pieces[node_index_to]["player_index"]
        if to_owner != player_index:
            # attack
            pass
        else:
            self.reinforce(player_index, num, node_index_to)
        
    def reinforce(self, num, node_index):
        player_index = self.cur_player
        self._check_valid_node(node_index)
        self._check_player_owns(player_index, node_index)
        self.pieces[node_index]["strength"] += num

    # player index
    cur_player = 0

    def next_turn(self):
        self.cur_turn = (self.cur_turn + 1) % len(self.players)
        print(f"turn {self.cur_turn}")


    def _check_valid_node(self, node_index):
        if node_index not in self.nodes:
            raise Exception("bad node")

    def _check_player_owns(self, player_index, node_index):
        if self.pieces[node_index]["player_index"] != player_index:
            raise Exception("does not belong to this player.")