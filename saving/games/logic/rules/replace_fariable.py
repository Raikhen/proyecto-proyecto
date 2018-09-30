def replace_fariable(game, theorem, fariable, formula):
    if not theorem in game.theorems:
        return False

    far_as_node = to_node(fariable, alphabet)

    if not far_as_node:
        return False

    if not to_node(formula, alphabet):
        return False

    if not far_as_node.symbol.equals(alphabet['fariable']):
        return False

    return theorem.replace(fariable, formula)
