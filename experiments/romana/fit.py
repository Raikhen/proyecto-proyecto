from tree.functions.to_node         import to_node
from tree.functions.to_string       import to_string
from tree.alphabets.logic           import get_logic_alphabet
from utils.get_random_logic_formula import get_random_logic_formula

'''
t1 and t2 stand for theorems
single_fit(t1, t2): This will fit t1 into t2.
double_fit(t1, t2): This will double-fit t1 and t2. If the two theorems
 don't double fit, this will return False. If the two theorems double fit, then it will return True for
 most cases but if the theorem are too large I suspect (it's an heuristic)
The way to solve this is simple but not easy to code. E.g. to double-fit A => (B => C) and (D => E) => D
 instead of storing A equals (D => E) we replace A for a pointer to (D => E). Thus, if we change something in
 (D => E), then the pointer stored in A will take into account the change.
'''

def fit(t1, t2, values1, values2, double_fit):
    alphabet = get_logic_alphabet()
    t1 = to_node(t1, alphabet) if type(t1) == str else t1
    t2 = to_node(t2, alphabet) if type(t2) == str else t2
    root1, root2 = t1.symbol.drawing, t2.symbol.drawing

    if root1 == root2 and root1 != 'F':
        if len(t1.children) == 1:
            return fit(t1.children[0], t2.children[0], values1, values2, double_fit)
        else:
            return fit(t1.children[0], t2.children[0], values1, values2, double_fit) \
               and fit(t1.children[1], t2.children[1], values1, values2, double_fit)
    elif root1 == 'F' and double_fit:
        values1.append((to_string(t1), to_string(t2)))
        return True
    elif root2 == 'F':
        values2.append((to_string(t2), to_string(t1)))
        return True
    else:
        return False

def simple_fit(t1, t2, double_fit):
    values1, values2 = [], []
    result = fit(t1, t2, values1, values2, double_fit)
    if result:
        t1, t2 = str(t1), str(t2)
        for fariable, formula in values1:
            t1 = t1.replace(fariable, formula)

        for fariable, formula in values2:
            t2 = t2.replace(fariable, formula)
        return t1 == t2, t1, t2
    else:
        return False, t1, t2

def full_fit(t1, t2, double_fit=True):
    i, fitted = 0, False
    while (not fitted) and i < 6:
        fitted, t1, t2 = simple_fit(t1, t2, double_fit)
        i += 1
    return fitted

single_fit = lambda t1, t2: simple_fit(t1, t2, double_fit=False)
double_fit = lambda t1, t2: full_fit(t1, t2)

def test_full_fit():
    assert full_fit('⇒(F_0, ⇒(F_1, F_2))', '⇒(⇒(F_3, F_4), F_5)')
    assert full_fit('⇒(F_0, ⇒(F_1, F_2))', '⇒(⇒(F_3, F_4), F_3)')
    assert full_fit('⇒(F_0, F_0)', '⇒(F_1, ⇒(F_2, F_3))')
    assert not full_fit('⇒(F_0, F_0)', '⇒(F_1, ⇒(F_1, F_2))')
    print('Test passed')
