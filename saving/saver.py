import os
import inspect
from game import Game

class Saver:
    @staticmethod
    def save_game(game, game_name):
        filename = f'saving/games/{game_name}/theorems.txt'
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as f:
            f.write('\n'.join(game.theorems))

        filename = f'saving/games/{game_name}/rules.txt'
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as f:
            f.write('\n'.join(game.rules.keys()))

        for [name, rule] in game.rules.items():
            filename = f'saving/games/{game_name}/rules/{name}.py'
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, 'w') as f:
                f.write(inspect.getsource(rule))

    @staticmethod
    def load_game(game_name):
        theorems = []
        rules = {}

        with open(f'saving/games/{game_name}/theorems.txt', 'r') as f:
            theorems = [theorem.strip() for theorem in f.readlines()]

        with open(f'saving/games/{game_name}/rules.txt', 'r') as f:
            rules = dict([[r.strip(), None] for r in f.readlines()])

        for name in rules:
            filename = f'saving.games.{game_name}.rules.{name}'
            module = __import__(filename, globals(), locals(), [name])
            rules[name] = getattr(module, name)

        return Game(rules, theorems)
