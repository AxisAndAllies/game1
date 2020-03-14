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



def move(player_index, num, node_index_from, node_index_to):
    _check_valid_node(node_index_from)
    _check_valid_node(node_index_to)
    _check_player_owns(player_index, node_index_from)
    to_owner = pieces[node_index_to]["player_index"]
    if to_owner != player_index:
        # attack
        pass
    else:
        reinforce(player_index, num, node_index_to)
    
def reinforce(player_index, num, node_index):
    _check_valid_node(node_index)
    _check_player_owns(player_index, node_index)
    pieces[node_index]["strength"] += num

# player index
cur_turn = 0

def next_turn():
    cur_turn = (cur_turn + 1)% len(players)
    print(f"turn {cur_turn}")


def _check_valid_node(node_index):
    if node_index not in nodes:
        raise Exception("bad to node")

def _check_player_owns(player_index, node_index):
    if pieces[node_index]["player_index"] != player_index:
        raise Exception("does not belong to this player.")