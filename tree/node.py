from tree.functions.to_string import to_string

class Node:
    def __init__(self, symbol, children = [], index = -1):
        self.symbol = symbol
        self.children = children
        self.index = index

    def equals(self, node):
        if not self.symbol.equals(node.symbol):
            return False

        if self.index != node.index:
            return False

        if len(self.children) != len(node.children):
            return False

        for i in range(0, len(self.children)):
            if not self.children[i].equals(node.children[i]):
                return False

        return True

    def __repr__(self):
        return to_string(self)
