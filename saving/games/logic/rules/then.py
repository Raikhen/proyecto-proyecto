def then(game, string):
    node = to_node(string, alphabet)

    if not node.symbol.equals(alphabet['implies']):
        return False

    if not string in game.theorems:
        return False

    if len(node.children) < 2:
        return False

    if not to_string(node.children[0]) in game.theorems:
        return False

    return to_string(node.children[1])
