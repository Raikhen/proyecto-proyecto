import time
import keyboard

def handle_root(games, params):
    keyboard.press_and_release('cmd+k')

    print('\nBienvenido, gilcito! Gracias por el audio! ¿Todo bien?\n')
    print('Escribí 1 para crear un juego.')
    print('Escribí 2 para acceder a un juego.')

    selection = 0
    not_an_int = False

    try:
        selection = int(input())
    except ValueError:
        not_an_int = True

    if not_an_int or not selection in [1, 2]:
        print('Tu mamá tiene cara de rana.\n')
        time.sleep(1)
        return '/'

    print()

    if selection == 1:
        return '/create-game'

    if selection == 2:
        return '/select-game'
