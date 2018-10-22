from numpy.random                   import choice

from saving.saver                   import Saver

def play(times = 1):
    game = Saver.load_game('numerals')

    for i in range(0, times):
        game.run_rule('next', choice(game.theorems))

    Saver.save_game(game, 'numerals')
