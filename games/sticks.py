from game   import Game

def get_sticks_game():
    axioms = ['|']

    def duplicate(game, theorem):
        if theorem in game.theorems:
            return theorem + theorem
        return False

    rules = {
        'duplicate': duplicate
    }

    return Game(rules, axioms)
