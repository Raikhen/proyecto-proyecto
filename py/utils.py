def is_theorem(game, conjecture):
    for theorem in game.theorems:
        if theorem == conjecture:
            return True
    return False
