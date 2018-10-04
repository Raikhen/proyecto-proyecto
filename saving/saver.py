import os
from game import Game

class Saver:
    @staticmethod
    def save_game(game, game_name):
        filename = f'saving/games/{game_name}/theorems.txt'
        os.makedirs(os.path.dirname(filename), exist_ok = True)

        with open(filename, 'w') as f:
            f.write('\n'.join(game.theorems))

        filename = f'saving/games/{game_name}/rules.txt'
        os.makedirs(os.path.dirname(filename), exist_ok = True)

        with open(filename, 'w') as f:
            f.write('\n'.join(game.rules.keys()))

        for name in game.rules:
            filename = f'saving/games/{game_name}/rules/{name}.py'
            os.makedirs(os.path.dirname(filename), exist_ok = True)

            with open(filename, 'w') as f:
                try:
                    f.write(game.rules_as_str[name])
                except:
                    return False

        return True

    @staticmethod
    def load_game(game_name):
        theorems = []
        rules = {}
        rules_as_str = {}

        with open(f'saving/games/{game_name}/theorems.txt', 'r') as f:
            theorems = [theorem.strip() for theorem in f.readlines()]

        with open(f'saving/games/{game_name}/rules.txt', 'r') as f:
            rules = dict([[r.strip(), None] for r in f.readlines()])

        for name in rules:
            import_name = f'saving.games.{game_name}.rules.{name}'
            module = __import__(import_name, globals(), locals(), [name])
            rules[name] = getattr(module, name)

            with open(f'saving/games/{game_name}/rules/{name}.py', 'r') as f:
                rules_as_str[name] = f.read()

        return Game(rules, theorems, False, rules_as_str)

    @staticmethod
    def get_games():
        with open('saving/games/index.txt', 'r') as f:
            games = {}
            games_names = [g.strip() for g in f.readlines()]
            
            for game_name in games_names:
                games[game_name] = Saver.load_game(game_name)

        return games
