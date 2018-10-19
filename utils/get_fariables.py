from tree.alphabets.logic   import get_logic_alphabet
from utils.get_leaves       import get_leaves

def get_fariables(node):
    alphabet = get_logic_alphabet()
    is_fariable = lambda n: n.symbol.equals(alphabet['fariable'])
    leaves = get_leaves(node)
    return list(filter(is_fariable, leaves))
