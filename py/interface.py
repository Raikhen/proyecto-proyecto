from games.logic.main import get_logic_game

class Interface:
    @staticmethod
    def init():
        print('Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?')

        logic = get_logic_game()
