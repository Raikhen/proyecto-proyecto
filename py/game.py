class Game:
    def __init__(self, rules, axioms, game = False):
        self.rules = {}
        self.theorems = []
  
        if game:
            self.theorems = game.theorems
            self.rules = game.rules

        self.rules.update(rules)
        self.theorems.extend(axioms)

    def run_rule(self, rule_name, *args):
        new_theorem = self.rules[rule_name](self, *args)

        if new_theorem and not new_theorem in self.theorems:
            self.theorems.append(new_theorem)
            return new_theorem

        return False

    def show_theorems(self):
        for theorem in self.theorems:
            print(theorem)
