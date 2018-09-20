from interface.root                 import handle_root
from interface.create.root          import handle_create_game
from interface.create.from_scratch  import handle_from_scratch

class Interface:
    games = []

    @staticmethod
    def init():
        print('\nBienvenido, gilcito! Gracias por el audio! ¿Todo bien?\n')

        paths = {
            '/': handle_root,
            '/create-game': handle_create_game,
            '/create-game/from-scratch': handle_from_scratch
        }

        path = '/'

        while True:
            path = paths[path](Interface.games)

'''
Crear juego
    - Con reglas de inferencia + axiomas
    - De una lista de funciones
    - Extender
    - Cargar juego
    - Atrás
Jugar juego
    - Usar regla de inferencia
    - Ver lista de teoremas
    - Ver reglas
    - Atrás
Guardar juego
    - Con teoremas
    - Sin teoremas

Con esta estructura que venís pensando, ¿donde vas a guardar los juegos?
'''
