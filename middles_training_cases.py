from pprint                         import pprint
from numpy.random                   import choice
from copy                           import deepcopy

from tree.functions.to_node         import to_node
from utils.get_fariables            import get_fariables
from games.logic.main               import get_logic_game
from tree.alphabets.logic           import get_logic_alphabet
from utils.get_random_logic_formula import get_random_logic_formula

'''
training_cases = [
    (
        (
            qvq,
            [axiom_1, axiom_2, axiom_3, ...]
        ),
        [midpoint_1, midpoint_2, midpoint_3, ...]
    )
]
'''

def get_weights_from_lens(theorems):
    weights = list(map(lambda t: len(t), theorems))
    weights = list(map(lambda x: 1 / x, weights))
    sum = 0

    for weight in weights:
        sum += weight

    for i in range(0, len(weights)):
        weights[i] /= sum

    return weights

def play(logic, times = 1):
    alphabet = get_logic_alphabet()

    graph = {
        '⇒(F_0, ⇒(F_1, F_0))': [],
        '⇒(⇒(F_0, ⇒(F_1, F_2)), ⇒(⇒(F_0, F_1), ⇒(F_0, F_2)))': [],
        '⇒(⇒(¬(F_0), ¬(F_1)), ⇒(F_1, F_0))': []
    }

    for i in range(0, times):
        rule_name = choice(['replace_fariable', 'then'])

        if rule_name == 'then':
            for theorem in logic.theorems:
                first_len = len(logic.theorems)
                logic.run_rule(rule_name, theorem)
                print('laruv2', logic.theorems[-1])
                if first_len != len(logic.theorems):
                    if not logic.theorems[-1] in graph.keys():
                        graph[logic.theorems[-1]] = []

                    a = str(to_node(theorem, alphabet).children[0])
                    graph[logic.theorems[-1]] += [theorem, a]

        elif rule_name == 'replace_fariable':
            weights = get_weights_from_lens(logic.theorems)
            theorem = choice(logic.theorems, p=weights)
            fariables = get_fariables(to_node(theorem, alphabet))
            fariable = str(choice(fariables))
            formula = str(get_random_logic_formula())
            first_len = len(logic.theorems)
            logic.run_rule(rule_name, theorem, fariable, formula)
            print('ramonete', theorem, 'ºººººººº', logic.theorems[-1], first_len, len(logic.theorems))
            if first_len != len(logic.theorems):
                if not logic.theorems[-1] in graph.keys():
                    graph[logic.theorems[-1]] = []
                graph[logic.theorems[-1]].append(theorem)

    return graph

def clean_proof(final_theorem, graph):
    to_process = set([final_theorem])
    marked = []
    print(final_theorem)

    while len(to_process):
        theorem = to_process.pop()

        for parent in graph[theorem]:
            print(theorem, parent)
            print()
            to_process.add(parent)

        marked.append(theorem)

    return marked

def get_training_cases():
    looping = 12, 4, 24
    training_cases = []

    for i in range(looping[0]):
        logic = get_logic_game()

        for j in range(looping[1]):
            axioms = deepcopy(logic.theorems)
            graph = play(logic, looping[2])
            final_theorem = logic.theorems[-1]
            print('se vienen')
            pprint(logic.theorems)
            theorems = clean_proof(final_theorem, graph)
            for theorem in axioms + [final_theorem]:
                if theorem in theorems:
                    theorems.remove(theorem)
            training_cases.append(((final_theorem, axioms), theorems))

    return training_cases

get_training_cases()

'''

Al hacerlo completamente al azar puede haber teoremas
intermedios que no sean usados para llegar al QVQ, así
que tenemos que corregir eso.

'''
