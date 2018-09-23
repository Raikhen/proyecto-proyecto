class Type:
    def __init__(self, type):
        self.name = type

    def equals(self, type):
        return self.name == type.name
