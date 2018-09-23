from unidecode      import unidecode
from game           import Game

def handle_create_game(games, params):
    axioms = []
    rules = {}
    template_game = False

    game_name = input('¿Cómo se va a llamar tu juego? ')

    print('¿Tu juego va extender a otro? (Se / See / Sí / No)', end=' ')
    extends_as_string = unidecode(input().lower())

    if extends_as_string in ['si', 'se', 'see']:
        if len(games):
            print('Estos son todos lo juegos creados:')

            for game in games:
                print(f'\t{game}')
            print()

            template_name = input('Nombre del juego que querés extender: ')

            if template_name in games.keys():
                template_game = games[template_name]
            else:
                print('Tu mamá tiene cara de rana.\n')
        else:
            print('No hay juegos creados.\n')

    elif extends_as_string == 'no':
        template_game = False
    else:
        print('La tia abuela de tu mejor amigx tiene cara de rana.')

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
    print()

    new_game = Game(rules, axioms, template_game)
    games[game_name] = new_game
    return '/'
