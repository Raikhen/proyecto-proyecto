def odd_rule(game, theorem):
    if theorem in game.theorems and len(theorem) % 6 == 4:
        return int((len(theorem) - 1) / 3) * '|'
    return False
