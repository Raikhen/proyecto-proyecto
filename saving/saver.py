import inspect
from game import Game

class Saver:
    @staticmethod
    def save_game(game, game_name):
        with open(f'saving/games/{game_name}.txt', 'w') as file:
            file.write(game_name)
            file.write('\n')
            file.write(str(len(game.rules)))
            file.write('\n')
            file.write(str(len(game.theorems)))

            file.write('\n\nRULES:\n\n')

            for rule_name, rule in game.rules.items():
                file.write(f'NAME: {rule_name}\n')
                file.write(f'FUNC:\n{inspect.getsource(rule)}')
                file.write('\n\n')

            file.write('\nTHEOREMS:\n\n')

            for theorem in game.theorems:
                file.write(theorem)
                file.write('\n')

    def load_game(game_name):
        with open(f'saving/games/{game_name}.txt') as file:
            file_as_string = file.read()
            lines = file_as_string.split('\n')

            rules_len = int(lines[1])
            theorems_len = int(lines[2])

            rules = {}

            x = file_as_string.find('RULES:')
            y = file_as_string.find('THEOREMS:')

            rules_section = file_as_string[x + len('RULES:'):y].strip()
            named_rules = rules_section[len('NAME: '):].split('NAME: ')

            for named_rule in named_rules:
                print(named_rule)
                print(named_rule.strip().split('\nFUNC:\n'))
                [name, rule_as_string] = named_rule.strip().split('\nFUNC:\n')
                exec(rule_as_string, globals())
                rules[name] = eval(name)

            print(rules)

            theorems_section = file_as_string[y + len('THEOREMS:'):]
            theorems = theorems_section.strip().split('\n')

            return Game(rules, theorems)
