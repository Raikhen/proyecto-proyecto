class Type:
    def __init__(self, type):
        self.name = type

    def equals(self, type):
        return self.name == type.name

    def to_string(self):
        return self.name

    def show(self):
        print(self.to_string())
