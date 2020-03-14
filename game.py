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
    if node_index_from not in nodes:
        raise Exception("bad from node")
    if node_index_to not in nodes:
        raise Exception("bad from node")
def reinforce(player_index, num, node_index):
    if node_index not in nodes:
        raise Exception("bad node")
    if pieces[node_index]["player_index"] != player_index:
        raise Exception("does not belong to this player.")
    pieces[node_index]["strength"] += num

# player index
cur_turn = 0

def next_turn():
    cur_turn = (cur_turn + 1)% len(players)
    print(f"turn {cur_turn}")
