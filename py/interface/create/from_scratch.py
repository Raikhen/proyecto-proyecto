from game import Game

def handle_from_scratch(games, params):
    axioms = []
    rules = {}

    game_name = input('¿Cómo se va a llamar tu juego? ')
    axioms_length = int(input('¿Cuantos axiomas va a tener tu juego? '))
    rules_length = int(input('¿Cuantas reglas va a tener tu juego? '))

    for i in range(0, axioms_length):
        axioms.append(input(f'Axioma {i + 1}: '))

    for i in range(0, rules_length):
        print(f'Regla {i + 1} (acordate que el primer parámetro es el juego):')
        rule_name = input('\tNombre de la regla: ')

        print('\tFunción (apretá Ctrl + D para guardar la regla):')
        lines = []

        while True:
            try:
                line = input('\t\t')
            except EOFError:
                break

            lines.append(line)

        rule ='\n'.join(lines)
        exec(rule, globals())
        rules[rule_name] = eval(rule_name)
        print()

    new_game = Game(rules, axioms)
    games[game_name] = new_game
    return '/'
