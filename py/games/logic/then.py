from tree.alphabets.logic import get_logic_alphabet

def then(game, implication):
    if implication.symbol.equals(get_logic_alphabet()['implies']):
        if implication in game.theorems:
            return False
