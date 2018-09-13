from games.sticks                   import get_sticks_game
from games.collatz                  import get_collatz_game
from games.logic                    import get_logic_game
from tree.alphabets.logic           import get_logic_alphabet
from tree.functions.to_tree         import to_tree
from tree.functions.to_string       import to_string

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        string = '⇒(⇒(F_0, F_1), ¬(F_1))'
        alphabet = get_logic_alphabet()

        node = to_tree(string, alphabet)
        print(string)
        print(to_string(node))
