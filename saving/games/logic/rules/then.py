def then(game, string):
    from tree.functions.to_node     import to_node
    from tree.alphabets.logic       import get_logic_alphabet

    alphabet = get_logic_alphabet()
    node = to_node(string, alphabet)

    if not node.symbol.equals(alphabet['implies']):
        return False

    if not string in game.theorems:
        return False

    if len(node.children) < 2:
        return False

    if not str(node.children[0]) in game.theorems:
        return False

    return str(node.children[1])
