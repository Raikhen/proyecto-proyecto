from game   import Game
from utils  import is_theorem

def get_sticks_game():
    axioms = ['|']

    def duplicate(game, theorem):
        if is_theorem(game, theorem):
            return theorem + theorem
        return False

    rules = {
        'duplicate': duplicate
    }

    return Game(rules, axioms)
