from games.sticks   import get_sticks_game
from games.collatz  import get_collatz_game
from games.logic    import get_logic_game

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        logic = get_logic_game()
