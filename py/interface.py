from games.sticks   import get_sticks_game
from games.collatz  import get_collatz_game
from games.logic    import get_logic_game

from tree.get_index import get_index

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        # logic = get_logic_game()

        print('get_index(\'⇒(F_0, F_1)\'):', get_index('⇒(F_0, F_1)'))
        print('get_index(\'F\'):', get_index('F'))
        print('get_index(\'F_0\'):', get_index('F_0'))
        print('get_index(\'F_0729\'):', get_index('F_0729'))
        print('get_index(\'F_-729\'):', get_index('F_-729'))
