class Game:
    nodes = {
        1: [2,3],
        2: [1,3],
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

        # must leave at least 1 behind
        if self.pieces[node_index_from]["strength"] <= num:
            raise Exception("not enough pieces to move")

        to_owner = self.pieces[node_index_to]["player_index"]
        self._substract_node_strength(node_index_from, num)
        if to_owner != player_index:
            # attack
            self._resolve_attack(num, node_index_to)
        else:
            self.reinforce(num, node_index_to)
        
    def reinforce(self, num, node_index):
        player_index = self.cur_player
        self._check_valid_node(node_index)
        self._check_player_owns(player_index, node_index)
        self._add_node_strength(node_index, num)

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

    
    def _resolve_attack(self, attacking_num, target_node_index) -> bool:
        '''
        returns whether attacker won.
        '''
        a = attacking_num
        b = self.pieces[target_node_index]["strength"]
        self._substract_node_strength(target_node_index, min(a,b))
        attacking_num -= min(a,b)
        return attacking_num > 0

    def _check_valid_unit_strength(self, num: int):
        if num < 0:
            raise Exception("negative units")
        if not isinstance(num, int):
            raise Exception("invalid unit strength type")

    def _add_node_strength(self, node_index, num: int):
        self._check_valid_node(node_index)
        self._check_valid_unit_strength(num)
        self.pieces[node_index]["strength"] += num

    def _substract_node_strength(self, node_index, num: int):
        self._check_valid_node(node_index)
        self._check_valid_unit_strength(num)
        self.pieces[node_index]["strength"] -= num