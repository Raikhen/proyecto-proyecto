class Type:
    def __init__(self, type):
        self.name = type

    def equals(self, type):
        return self.name == type.name

    def __repr__(self):
        return self.name
