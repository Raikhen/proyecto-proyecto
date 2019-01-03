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

def play(logic, times):
    logic.theorems = [choice(logic.theorems)]# We select one axiom at random

    for i in range(times):
        alphabet = get_logic_alphabet()
        theorem = logic.theorems[-1]
        fariables = get_fariables(to_node(theorem, alphabet))
        fariable = str(choice(fariables))
        formula = fariable
        while formula == fariable:
            formula = str(get_random_logic_formula())
        logic.run_rule('replace_fariable', theorem, fariable, formula)

def get_training_case():
    lengths = sen_max_length + 1
    while lengths > sen_max_length:
        logic = get_logic_game()
        logic.theorems = []
        while len(logic.theorems) < 3:
            logic = get_logic_game()
            play(logic, 2)
        axiom, theorem, qvq = logic.theorems
        axiom, qvq = [vectorize(t) for t in [axiom, qvq]]
        theorem = vectorize(theorem, hot=False)
        lengths = max([len(t) for t in [axiom, qvq, theorem]])
    return [axiom, qvq], theorem

def get_training_batch():
    cases = [get_training_case() for i in range(32)]
    xs, ys = zip(*cases)
    return xs, ys

chars = ['(', ')', '⇒', ',', '¬', '|', '-']# | is a stick for variables. - es para rellenar
chars_to_i = {c: i for i, c in enumerate(chars)}
sen_max_length = 60

def vectorize(theorem, hot=True):
    theorem = theorem.replace(' ', '')
    match = True
    print(theorem)
    while match:
        match = re.search(r'F_[0-9]+[^0-9]', theorem)
        if match:
            fariable = theorem[match.start():match.end()]
            sticks = '|' * (int(fariable[2:-1]) + 1)
            theorem = theorem.replace(fariable, sticks + fariable[-1])
    print(theorem)
    theorem = theorem + '-' * (sen_max_length - len(theorem))
    if hot:
        theorem = [one_hot(c) for c in theorem]
        return np.array(theorem)
    else:
        return theorem

def one_hot(char):
    pos = chars_to_i[char]
    array = np.zeros((len(chars)))
    array[pos] = 1
    return array

class MiddleTask:
    def __init__(self):
        self.batches = np.load('batches.npy')
        self.i = 0

    def next_batch(self):
        self.i += 1
        if self.i >= len(self.batches):
            self.i = 0
        xs, ys = self.batches[self.i]
        xs = np.array([np.array(x) for x in xs])
        ys = np.array([np.array(y) for y in ys])
        return xs, ys

'''
batches = []
for i in range(100):
    batches.append(get_training_batch())
    print(i)
'''
