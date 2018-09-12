from game                   import Game
from tree.alphabets.logic   import get_logic_alphabet

def get_logic_game():
    axioms = [
        '⇒(F_0, ⇒(F_1, F_0))',
        '⇒(⇒(F_0, ⇒(F_1, F_2)), ⇒(⇒(F_0, F_1), ⇒(F_0, F_2)))',
        '⇒(⇒(¬(F_0), ¬(F_1)), ⇒(F_1, F_0))'
    ]

    def replace_fariable(game, theorem, fariable, formula):
        if theorem in game.theorems:
            return True
        return False

    def then(game, implication):
        return False

    rules = {
        'replace_fariable': replace_fariable,
        'then': then
    }

    return Game(rules, axioms)
