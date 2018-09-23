from interface.root                 import handle_root
from interface.create.root          import handle_create_game
from interface.play.select          import handle_select_game
from interface.play.root            import handle_play_game
from interface.play.show_theorems   import handle_show_theorems
from games.collatz                  import get_collatz_game
from games.sticks                   import get_sticks_game
from games.logic.main               import get_logic_game

class Interface:
    games = {}

    @staticmethod
    def init():
        print('\nBienvenido, gilcito! Gracias por el audio! ¿Todo bien?\n')

        Interface.games.update({
            'collatz': get_collatz_game(),
            'sticks': get_sticks_game(),
            'logic': get_logic_game()
        })

        paths = {
            '/': handle_root,
            '/create-game': handle_create_game,
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
