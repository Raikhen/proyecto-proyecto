import time
from inspect        import signature
from saving.saver   import Saver

def handle_use_rule(games, params):
    game_name = params['game_name']
    game = games[game_name]

    if not len(game.rules):
        print(f'{game_name} no tiene reglas de inferencia.\n')
        return '/'

    print(f'Estas son todas las reglas de {game_name}:')

    for rule in game.rules.keys():
        print(f'\t{rule}')
    print()

    rule_name = input('Nombre de la regla que querés usar: ')

    if not rule_name in game.rules.keys():
        print('Tu mamá tiene cara de rana.\n')
        time.sleep(1)
        return '/'

    rule = game.rules[rule_name]
    parameters = list(signature(rule).parameters.keys())[1:]
    arguments = []

    for parameter in parameters:
        arguments.append(input(f'Valor del parámetro "{parameter}": '))

    game.run_rule(rule_name, *arguments)
    Saver.save_game(game, game_name)

    print()
    return f'/play-game?game_name={game_name}'
