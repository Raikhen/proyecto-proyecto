from saving.saver                   import Saver
from interface.root                 import handle_root
from interface.create.root          import handle_create_game
from interface.play.select          import handle_select_game
from interface.play.root            import handle_play_game
from interface.play.show_theorems   import handle_show_theorems
from interface.play.show_rules      import handle_show_rules
from interface.play.use_rule        import handle_use_rule

class Interface:
    games = Saver.get_games()

    @staticmethod
    def init():
        paths = {
            '/': handle_root,
            '/create-game': handle_create_game,
            '/select-game': handle_select_game,
            '/play-game': handle_play_game,
            '/play-game/show-theorems': handle_show_theorems,
            '/play-game/show-rules': handle_show_rules,
            '/play-game/use-rule': handle_use_rule
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
