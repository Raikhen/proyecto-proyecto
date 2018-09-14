from games.logic.main import get_logic_game

class Interface:
    @staticmethod
    def init():
        print('\nBienvenido, gilcito! Gracias por el audio! ¿Todo bien?\n')

        logic = get_logic_game()
        logic.show_theorems()
        print()

        theorem = logic.theorems[0]
        fariable = 'F_0'
        formula = '⇒(F_1, F_0)'

        logic.run_rule('replace_fariable', theorem, fariable, formula)
        logic.show_theorems()
        print()
