def replace_fariable(game, theorem, fariable, formula):
    from tree.functions.to_node import to_node
    from tree.alphabets.logic   import get_logic_alphabet

    alphabet = get_logic_alphabet()

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
