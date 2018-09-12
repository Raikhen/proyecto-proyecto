from tree.functions.get_index       import get_index
from tree.functions.get_children    import get_children

def to_tree(string, alphabet):
    node = False
    symbol = False
    index = -1

    if len(string):
        drawing = string[0]

        for alphabet_symbol in alphabet:
            if alphabet_symbol.drawing == drawing:
                symbol = alphabet_symbol

        if symbol:
            if len(string) > 1 and string[1] == '_':
                index = get_index(string)

                if index == -1:
                    return False

            # TODO: get_children(string)

    return False
