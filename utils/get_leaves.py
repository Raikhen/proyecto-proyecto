from tree.functions.to_node     import to_node
from tree.alphabets.logic       import get_logic_alphabet

def get_leaves(node):
    if len(node.children) == 0:
        return [node]

    alphabet = get_logic_alphabet()
    leaves = []

    def to_logic_node(string):
        return to_node(string, alphabet)

    for child in node.children:
        leaves.extend(get_leaves(child))

    leaves = list(map(str, leaves))
    leaves = list(set(leaves))
    leaves = list(map(to_logic_node, leaves))
    return leaves
