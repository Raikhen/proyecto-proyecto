from tree.alphabets.logic           import get_logic_alphabet
from tree.functions.to_tree         import to_tree
from tree.functions.to_string       import to_string

from tree.node                      import Node
from tree.symbol                    import Symbol
from tree.type                      import Type

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        type_1 = Type('FORMULA')
        type_2 = Type('FORMULA')
        type_3 = Type('VARIABLE')

        print('\nType testing:')
        print(type_1.equals(type_2))
        print(type_1.equals(type_3))
        print(type_2.equals(type_3))

        symbol_1 = Symbol('x', type_1, [type_3, type_3])
        symbol_2 = Symbol('x', type_2, [type_3, type_3])
        symbol_3 = Symbol('y', type_1, [type_3, type_3])
        symbol_4 = Symbol('x', type_3, [type_3, type_3])
        symbol_5 = Symbol('x', type_1, [type_2, type_3])

        print('\nSymbol testing:')
        print(symbol_1.equals(symbol_2))
        print(symbol_1.equals(symbol_3))
        print(symbol_1.equals(symbol_4))
        print(symbol_1.equals(symbol_5))

        # No agregué tests para nodes pero al dope, va a funcar.

        print('\n')

        '''
        string = '⇒(⇒(F_0, F_1), ¬(F_1))'
        alphabet = get_logic_alphabet()

        node = to_tree(string, alphabet)
        print(string)
        print(to_string(node))
        '''
