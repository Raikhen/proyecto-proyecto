import inspect

def handle_show_rules(games, params):
    game_name = params['game_name']
    game = games[game_name]

    '''
    print(f'Las reglas de inferencia de {game_name} son:')

    for rule_name, rule in game.rules.items():
        code = inspect.getsource(rule).replace('\n', '\n\t\t')

        print(f'\n\t{rule_name}:')
        print(f'\t\t{code}')

    print()
    '''

    print('En reparación...\n')

    return f'/play-game?game_name={game_name}'
