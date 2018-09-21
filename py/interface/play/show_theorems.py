def handle_show_theorems(games, params):
    game_name = params['game_name']
    game = games[game_name]

    print(f'Los teoremas de {game_name} son:')

    for theorem in game.theorems:
        print(f'\t{theorem}')

    print()

    return f'/play-game?game_name={game_name}'
