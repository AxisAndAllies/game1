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

def move(owner, num):
    pass

def reinforce(owner, num, node_index):
    if node_index not in nodes:
        raise Exception("bad node")
    nodes[node_index]
    pass

# player index
cur_turn = 0

def next_turn():
    cur_turn = (cur_turn + 1)% len(players)
    print(f"turn {cur_turn}")
