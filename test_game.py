from game import Game

def test_game():
    g = Game()
    
    UNITS = 3
    FROM_TERRITORY = 1
    TO_TERRITORY = 2

    g.move(
        UNITS,
        FROM_TERRITORY,
        TO_TERRITORY
    )