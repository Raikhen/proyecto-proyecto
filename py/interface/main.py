from interface.root                 import handle_root
from interface.create.root          import handle_create_game
from interface.create.from_scratch  import handle_from_scratch
from interface.play.select          import handle_select_game
from interface.play.root            import handle_play_game
from interface.play.show_theorems   import handle_show_theorems

class Interface:
    games = {}

    @staticmethod
    def init():
        print('\nBienvenido, gilcito! Gracias por el audio! ¿Todo bien?\n')

        paths = {
            '/': handle_root,
            '/create-game': handle_create_game,
            '/create-game/from-scratch': handle_from_scratch,
            '/select-game': handle_select_game,
            '/play-game': handle_play_game,
            '/play-game/show-theorems': handle_show_theorems
        }

        path = '/'
        params = {}

        while True:
            path = paths[path](Interface.games, params)
            params = {}

            if path.find('?') > -1:
                params_as_list = path[path.find('?') + 1:].split('&')

                for param in params_as_list:
                    [key, value] = param.split('=')
                    params[key] = value

                path = path[:path.find('?')]

'''
Crear juego
    - Con reglas de inferencia + axiomas
    - De una lista de funciones
    - Extender
    - Cargar juego
    - Atrás
Seleccionar juego
    - Usar regla de inferencia
    - Ver lista de teoremas
    - Ver reglas
    - Atrás
Guardar juego
    - Con teoremas
    - Sin teoremas

'''
