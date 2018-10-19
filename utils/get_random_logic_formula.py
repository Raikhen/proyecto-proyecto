import random
from numpy.random               import choice

from tree.node                  import Node
from tree.alphabets.logic       import get_logic_alphabet

def get_random_logic_formula():
    alphabet = get_logic_alphabet()
    options = ['fariable', 'implies', 'not']
    options_weights = [0.75, 0.125, 0.125]
    chosen = choice(options, p=options_weights)

    if chosen == 'fariable':
        indexes = range(0, 10000)
        weights = []

        for i in indexes:
            weights.append(0.5 ** (i + 1))

        index = choice(indexes, p=weights)
        return Node(alphabet[chosen], index=index)

    elif chosen == 'implies':
        child_1 = get_random_logic_formula()
        child_2 = get_random_logic_formula()
        children = [child_1, child_2]
        return Node(alphabet[chosen], children)

    elif chosen == 'not':
        children = [get_random_logic_formula()]
        return Node(alphabet[chosen], children)
