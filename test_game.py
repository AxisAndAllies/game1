from game import Game


def setup_game(g):
    setup = {
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


def test_attack():
    g = Game()

    UNITS = 3
    FROM_TERRITORY = 1
    TO_TERRITORY = 3  # enemy territory

    original_units_a = g.pieces[FROM_TERRITORY]['strength']
    original_units_b = g.pieces[TO_TERRITORY]['strength']

    g.move(UNITS, FROM_TERRITORY, TO_TERRITORY)

    new_units_a = g.pieces[FROM_TERRITORY]['strength']
    new_units_b = g.pieces[TO_TERRITORY]['strength']

    print('Original units:', original_units_a, original_units_b)
    print('New units:', new_units_a, new_units_b)

    if original_units_a + original_units_b <= new_units_a + new_units_b:
        raise ValueError('Some units have to die!')


def test_move():
    g = Game()

    UNITS = 3
    FROM_TERRITORY = 1
    TO_TERRITORY = 2

    original_units_a = g.pieces[FROM_TERRITORY]['strength']
    original_units_b = g.pieces[TO_TERRITORY]['strength']

    g.move(UNITS, FROM_TERRITORY, TO_TERRITORY)

    new_units_a = g.pieces[FROM_TERRITORY]['strength']
    new_units_b = g.pieces[TO_TERRITORY]['strength']

    print('Original units:', original_units_a, original_units_b)
    print('New units:', new_units_a, new_units_b)

    if original_units_a + original_units_b != new_units_a + new_units_b:
        raise ValueError('Units must be conserved')

    if original_units_a - new_units_a != UNITS:
        raise ValueError("Didn't move {} units".format(UNITS))


test_move()
test_attack()