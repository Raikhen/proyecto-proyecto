from game           import Game
from games.sticks   import get_sticks_game

def odd_rule(game, theorem):
    if theorem in game.theorems and len(theorem) % 6 == 4:
        return int((len(theorem) - 1) / 3) * '|'
    return False

def get_collatz_game():
    new_rules = {
        'odd_rule': odd_rule
    }

    return Game(new_rules, [], get_sticks_game())
