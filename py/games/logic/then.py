from tree.functions.to_node     import to_node
from tree.functions.to_string   import to_string
from tree.alphabets.logic       import get_logic_alphabet

def then(game, string):
    node = to_node(string, get_logic_alphabet())

    if not node.symbol.equals(get_logic_alphabet()['implies']):
        return False

    if not string in game.theorems:
        return False

    if len(node.children) < 2:
        return False

    if not to_string(node.children[0]) in game.theorems:
        return False

    return to_string(node.children[1])
