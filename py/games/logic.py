from game import Game

'''
class Type:
    def __init__(type):
        if
'''

def get_logic_game():
    axioms = [
        '⇒(F_0, ⇒(F_1, F_0))',
        '⇒(⇒(F_0, ⇒(F_1, F_2)), ⇒(⇒(F_0, F_1), ⇒(F_0, F_2)))',
        '⇒(⇒(¬(F_0), ¬(F_1)), ⇒(F_1, F_0))'
    ]

    def replace_fariable(game, fariable, formula):
        return False

    def then(game, implication):
        return False

    rules = {
        'replace_fariable': replace_fariable,
        'then': then
    }

    return Game(rules, axioms)

'''
Idea: tal vez la posta es hacer otro sistema que tenga
como teoremas a todos los enunciados válidos.

Tal vez hasta se podría hacer otro sistema que tenga
como teoremas a todas las fórmulas válidas, como paso
intermedio.
'''
