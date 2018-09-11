from game   import Game
from utils  import is_theorem
from sticks import get_sticks_game

def get_collatz_game():
    def odd_rule(game, theorem):
        if is_theorem(game, theorem) and len(theorem) % 6 == 4:
            return int((len(theorem) - 1) / 3) * '|'
        return False

    new_rules = {
        'odd_rule': odd_rule
    }

    return Game(new_rules, [], get_sticks_game())
