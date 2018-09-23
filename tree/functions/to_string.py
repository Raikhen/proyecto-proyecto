def to_string(node):
    string = node.symbol.drawing

    if node.index > -1:
        string += '_{}'.format(node.index)

    if len(node.children) > 0:
        string += '('

        for child in node.children:
            string += '{}, '.format(to_string(child))

        string = string[:-2]
        string += ')'

    return string
