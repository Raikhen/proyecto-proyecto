from game   import Game

def duplicate(game, theorem):
    if theorem in game.theorems:
        return theorem + theorem
    return False

def get_sticks_game():
    axioms = ['|']

    rules = {
        'duplicate': duplicate
    }

    return Game(rules, axioms)
