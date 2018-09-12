from games.sticks                   import get_sticks_game
from games.collatz                  import get_collatz_game
from games.logic                    import get_logic_game
from tree.alphabets.logic           import get_logic_alphabet
from tree.functions.to_tree         import to_tree

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        string = '⇒(⇒(F_0, F_1), ¬(F_1))'
        alphabet = get_logic_alphabet()

        print(to_tree(string, alphabet).children[1].symbol.drawing)
