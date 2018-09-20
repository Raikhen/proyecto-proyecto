from game import Game

def handle_from_scratch(games):
    axioms = []
    rules = {}

    axioms_length = int(input('¿Cuantos axiomas va a tener tu juego? '))
    rules_length = int(input('¿Cuantas reglas va a tener tu juego? '))

    for i in range(0, axioms_length):
        axioms.append(input(f'Axioma {i + 1}: '))

    for i in range(0, rules_length):
        print(f'Regla {i + 1} (acordate que el primer parámetro es el juego):')
        name = input('\tNombre de la regla: ')

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
        rules[name] = eval(name)

    new_game = Game(rules, axioms)
    games.append(new_game)
    return '/'
