from pprint                         import pprint
from numpy.random                   import choice
from copy                           import deepcopy

from tree.functions.to_node         import to_node
from utils.get_fariables            import get_fariables
from games.logic.main               import get_logic_game
from tree.alphabets.logic           import get_logic_alphabet
from utils.get_random_logic_formula import get_random_logic_formula
import re
import numpy as np
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
                # print('from then', logic.theorems[-1], '|||', theorem, first_len, len(logic.theorems))
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
            # print('from replace', logic.theorems[-1], '|||', theorem, first_len, len(logic.theorems))
            if first_len != len(logic.theorems):
                if not logic.theorems[-1] in graph.keys():
                    graph[logic.theorems[-1]] = []
                graph[logic.theorems[-1]].append(theorem)

    return graph

def clean_proof(final_theorem, graph):
    to_process = set([final_theorem])
    marked = []
    # print(final_theorem)

    while len(to_process):
        theorem = to_process.pop()

        for parent in graph[theorem]:
            to_process.add(parent)

        marked.append(theorem)

    return marked

def generate_training_cases():
    looping = 12

    logic = get_logic_game()
    axioms = deepcopy(logic.theorems)
    graph = play(logic, looping)
    final_theorem = logic.theorems[-1]

    print(final_theorem)
    theorems = clean_proof(final_theorem, graph)
    print(theorems)
    for theorem in axioms + [final_theorem]:
        if theorem in theorems:
            theorems.remove(theorem)

    # print(final_theorem, theorems, axioms)
    stop
    final_theorem = vectorize(final_theorem)
    axioms = [vectorize(axiom) for axiom in axioms]
    # theorems = [vectorize(theorem) for theorem in theorems]

    return (final_theorem, *axioms), theorems

def get_training_cases():
    correct = True
    while correct:
        output = generate_training_cases()
        correct = len(output[1]) == 0
    return output

chars = ['(', ')', '⇒', ',', '¬', '|', '-']# | is a stick for variables. - es para rellenar
chars_to_i = {c: i for i, c in enumerate(chars)}
sen_max_length = 300

def vectorize(theorem):
    theorem = theorem.replace(' ', '')
    match = True
    while match:
        match = re.search(r'F_[0-9]+', theorem)
        if match:
            fariable = theorem[match.start():match.end()]
            sticks = '|' * (int(fariable[2:]) + 1)
            theorem = theorem.replace(fariable, sticks)
    theorem = theorem + '-' * (sen_max_length - len(theorem))
    vector = [one_hot(c) for c in theorem]
    return np.array(vector)

def one_hot(char):
    pos = chars_to_i[char]
    array = np.zeros((len(chars)))
    array[pos] = 1
    return array

'''

Al hacerlo completamente al azar puede haber teoremas
intermedios que no sean usados para llegar al QVQ, así
que tenemos que corregir eso.

'''
