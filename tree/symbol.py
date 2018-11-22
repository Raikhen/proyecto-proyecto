class Symbol:
    def __init__(self, drawing, type, children_format = []):
        self.drawing = drawing
        self.type = type
        self.children_format = children_format

    def equals(self, symbol):
        if self.drawing != symbol.drawing:
            return False

        if not self.type.equals(symbol.type):
            return False

        if len(self.children_format) != len(symbol.children_format):
            return False

        for i in range(0, len(self.children_format)):
            if not self.children_format[i].equals(symbol.children_format[i]):
                return False

        return True

    def __repr__(self):
        children = list(map(str, self.children_format))
        children = ', '.join(children)
        return f'{self.drawing} : ({children}) ⇒ {str(self.type)}'
