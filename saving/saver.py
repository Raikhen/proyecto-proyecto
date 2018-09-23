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
            file.write('\n\n')

            for rule in game.rules.values():
                file.write(inspect.getsource(rule))
                file.write('\n\n')

            for theorem in game.theorems:
                file.write(theorem)
                file.write('\n')

    def load_game(game_name):
        return False
