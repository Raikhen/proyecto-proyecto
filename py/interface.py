from games.sticks                   import get_sticks_game
from games.collatz                  import get_collatz_game
from games.logic                    import get_logic_game

from tree.functions.get_children    import get_children

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        print('get_children(\'⇒(F_0, F_1)\'):', get_children('⇒(F_0, F_1)'))
        print('get_children(\'⇒(⇒(F_0, F_1), F_1)\'):', get_children('⇒(⇒(F_0, F_1), F_1)'))
        print('get_children(\'¬(F_0)\'):', get_children('¬(F_0)'))
        print('get_children(\'F\'):', get_children('F'))
        print('get_children(\'F_0\'):', get_children('F_0'))
        print('get_children(\'F_0729\'):', get_children('F_0729'))
        print('get_children(\'F_-729\'):', get_children('F_-729'))
        print('get_children(\'⇒(⇒(F_0, F_1), ¬(F_1))\'):', get_children('⇒(⇒(F_0, F_1), ¬(F_1))'))
        print('get_children(\'⇒(⇒(F_0, )F_1), ¬(F_1))\'):', get_children('⇒(⇒(F_0, )F_1), ¬(F_1))'))
