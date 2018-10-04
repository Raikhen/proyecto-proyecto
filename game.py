import inspect

class Game:
    def __init__(self, rules, axioms, game = False, rules_as_str = False):
        self.rules = {}
        self.theorems = []
        self.rules_as_str = {}

        if game:
            self.theorems = game.theorems
            self.rules = game.rules
            self.rules_as_str = game.rules_as_str

        self.rules.update(rules)
        self.theorems.extend(axioms)

        if not rules_as_str or len(rules) > len(rules_as_str):
            try:
                for [name, rule] in rules.items():
                    self.rules_as_str[name] = inspect.getsource(rule)
            except:
                pass
        else:
            self.rules_as_str.update(rules_as_str)

    def run_rule(self, rule_name, *args):
        new_theorem = self.rules[rule_name](self, *args)

        if new_theorem and not new_theorem in self.theorems:
            self.theorems.append(new_theorem)
            return new_theorem

        return False

    def show_theorems(self):
        for theorem in self.theorems:
            print(theorem)
