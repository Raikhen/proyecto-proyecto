import time

def handle_play_game(games, params):
    game_name = params['game_name']
    game = games[game_name]

    print('Escribí 1 para ver todos los teoremas.')
    print('Escribí 2 para ver todas las reglas de inferencia.')
    print('Escribí 3 para usar alguna regla de inferencia.')
    print('Escribí 4 para ir atrás.')

    selection = 0
    not_an_int = False

    try:
        selection = int(input())
    except ValueError:
        not_an_int = True

    if not_an_int or not selection in [1, 2, 3, 4]:
        print('Tu mamá tiene cara de rana.\n')
        time.sleep(1)
        return '/'

    print()

    if selection == 1:
        return f'/play-game/show-theorems?game_name={game_name}'

    if selection == 2:
        return f'/play-game/show-rules?game_name={game_name}'

    if selection == 3:
        return f'/play-game/use-rule?game_name={game_name}'

    if selection == 4:
        return '/'
