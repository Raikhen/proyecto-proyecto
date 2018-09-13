from game                           import Game
from games.logic.then               import then
from games.logic.replace_fariable   import replace_fariable
from tree.alphabets.logic           import get_logic_alphabet

def get_logic_game():
    axioms = [
        '⇒(F_0, ⇒(F_1, F_0))',
        '⇒(⇒(F_0, ⇒(F_1, F_2)), ⇒(⇒(F_0, F_1), ⇒(F_0, F_2)))',
        '⇒(⇒(¬(F_0), ¬(F_1)), ⇒(F_1, F_0))'
    ]

    rules = {
        'replace_fariable': replace_fariable,
        'then': then
    }

    return Game(rules, axioms)
