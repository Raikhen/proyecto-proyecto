def handle_create_game(games):
    print('Escribí 1 para crear un juego desde cero.')
    print('Escribí 2 para crear un juego preformateado.')
    print('Escribí 3 para crear un juego extendiendo otro.')
    print('Escribí 4 para ir atrás.')

    selection = 0
    not_an_int = False

    try:
        selection = int(input())
    except ValueError:
        not_an_int = True

    if not_an_int or not selection in [1, 2, 3, 4]:
        print('Tu mamá tiene cara de rana.\n')
        return '/'

    print()

    if selection == 1:
        return '/create-game/from-scratch'

    if selection == 2:
        return '/create-game/preformatted'

    if selection == 3:
        return '/create-game/extend'

    if selection == 4:
        return '/'
