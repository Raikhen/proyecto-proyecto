from tree.type      import Type
from tree.symbol    import Symbol

def get_logic_alphabet():
    formula = Type('FORMULA')

    not_symbol = Symbol('¬', formula, [formula])
    implies_symbol = Symbol('⇒', formula, [formula, formula])
    fariable_symbol = Symbol('F', formula)

    return {
        'not': not_symbol,
        'implies': implies_symbol,
        'fariable': fariable_symbol
    }
