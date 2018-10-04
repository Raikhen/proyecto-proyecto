import time

def handle_select_game(games, params):
    if not len(games):
        print('No hay juegos creados.\n')
        return '/'

    print('Estos son todos lo juegos creados:')

    for game in games:
        print(f'\t{game}')
    print()

    game_name = input('Nombre del juego que querés jugar: ')

    if not game_name in games.keys():
        print('Tu mamá tiene cara de rana.\n')
        time.sleep(1)
        return '/'

    print()
    return f'/play-game?game_name={game_name}'
