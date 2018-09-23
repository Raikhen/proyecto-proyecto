from tree.node                      import Node
from tree.functions.get_index       import get_index
from tree.functions.get_children    import get_children

def to_node(string, alphabet):
    symbol = False
    index = -1
    children = []

    if len(string):
        drawing = string[0]

        for alphabet_symbol in alphabet.values():
            if alphabet_symbol.drawing == drawing:
                symbol = alphabet_symbol

        if symbol:
            if len(string) > 1 and string[1] == '_':
                index = get_index(string)

                if index == -1:
                    return False

            children_as_strings = get_children(string)

            if children_as_strings:
                for child_as_string in children_as_strings:
                    children.append(to_node(child_as_string, alphabet))

            return Node(symbol, children, index)

    return False
