def duplicate(game, theorem):
    if theorem in game.theorems:
        return theorem + theorem
    return False
