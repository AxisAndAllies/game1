class Game:
    graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}

    players = ['a', 'b']

    def __init__(self):
        self.player_territories = dict()
        self.pieces = dict()

    # player index
    cur_player = 0

    def get_state(self):
        return {
            'current': self.cur_player,
            'graph': self.graph,
            'players': self.players,
            'player_territories': self.player_territories,
            'pieces': self.pieces
        }

    def _check_connected(self, from_index, to_index):
        if to_index not in self.graph[from_index]:
            raise Exception("Territories are not connected!")

    def move(self, num, node_index_from, node_index_to):
        player_index = self.cur_player
        self._check_valid_node(node_index_from)
        self._check_valid_node(node_index_to)
        self._check_valid_unit_strength(num)
        self._check_connected(node_index_from, node_index_to)
        self._check_player_owns(player_index, node_index_from)

        # must leave at least 1 behind
        if self.pieces[node_index_from]["strength"] <= num:
            raise Exception("not enough pieces to move")

        to_owner = self.pieces[node_index_to]["player_index"]
        self.pieces[node_index_from]["strength"] -= num
        if to_owner != player_index:
            # attack
            self._resolve_attack(num, node_index_to)
        else:
            self.reinforce(num, node_index_to)

    def reinforce(self, num, node_index):
        player_index = self.cur_player
        self._check_valid_node(node_index)
        # for initially adding units to unclaimed territories
        if node_index in self.pieces:
            self._check_player_owns(player_index, node_index)
        self._add_node_strength(node_index, num)

    def next_turn(self):
        self.cur_player = (self.cur_player+ 1) % len(self.players)
        print(f"turn {self.cur_player}")

    def _check_valid_node(self, node_index):
        if node_index not in self.graph:
            raise Exception("bad node")

    def _check_player_owns(self, player_index, node_index):
        if self.pieces[node_index]["player_index"] != player_index:
            raise Exception("does not belong to this player.")

    def _resolve_attack(self, attacking_num, target_node_index) -> bool:
        '''
        returns whether attacker won.
        '''
        a = attacking_num
        b = self.pieces[target_node_index]["strength"]
        self._substract_node_strength(target_node_index, min(a, b))
        attacking_num -= min(a, b)
        
        won = attacking_num > 0
        if won:
            self.pieces[target_node_index]['player_index'] = self.cur_player
            self._add_node_strength(target_node_index, attacking_num)
        return won

    def _check_valid_unit_strength(self, num: int):
        if not isinstance(num, int):
            raise Exception("invalid unit strength type")
        if num < 0:
            raise Exception("negative units")

    def _add_node_strength(self, node_index, num: int):
        self.pieces[node_index]["strength"] += num

    def _substract_node_strength(self, node_index, num: int):
        self.pieces[node_index]["strength"] -= num