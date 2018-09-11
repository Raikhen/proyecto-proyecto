from sticks     import get_sticks_game
from collatz    import get_collatz_game

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        print('Boludeando con el juego de los palitos:')
        sticks_game = get_sticks_game()
        sticks_game.run_rule('duplicate', '|')
        sticks_game.run_rule('duplicate', '||')
        print(sticks_game.theorems)

        print('Boludeando con el juego de collatz:')
        collatz_game = get_collatz_game()
        collatz_game.run_rule('duplicate', '|')
        collatz_game.run_rule('duplicate', '||')
        collatz_game.run_rule('duplicate', '||||')
        collatz_game.run_rule('duplicate', '||||||||')
        collatz_game.run_rule('odd_rule', '||||||||||||||||')
        print(collatz_game.theorems)
