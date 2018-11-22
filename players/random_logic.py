from numpy.random                   import choice

from saving.saver                   import Saver
from tree.functions.to_node         import to_node
from utils.get_fariables            import get_fariables
from tree.alphabets.logic           import get_logic_alphabet
from utils.get_random_logic_formula import get_random_logic_formula

def get_weights_from_lens(theorems):
    weights = list(map(lambda t: len(t), theorems))
    weights = list(map(lambda x: 1 / x, weights))
    sum = 0

    for weight in weights:
        sum += weight

    for i in range(0, len(weights)):
        weights[i] /= sum

    return weights

def play(times = 1):
    alphabet = get_logic_alphabet()
    logic = Saver.load_game('logic')

    for i in range(0, times):
        rule_name = choice(['replace_fariable', 'then'])

        if rule_name == 'then':
            for theorem in logic.theorems:
                logic.run_rule(rule_name, theorem)
        elif rule_name == 'replace_fariable':
            weights = get_weights_from_lens(logic.theorems)
            theorem = choice(logic.theorems, p=weights)
            fariables = get_fariables(to_node(theorem, alphabet))
            fariable = str(choice(fariables))
            formula = str(get_random_logic_formula())
            logic.run_rule(rule_name, theorem, fariable, formula)

    Saver.save_game(logic, 'logic')
