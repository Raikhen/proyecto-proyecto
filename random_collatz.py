import random
from saving.saver import Saver

collatz = Saver.load_game('collatz')
LOOP_TIMES = 999

for i in range(0, LOOP_TIMES):
    rule_name = random.choice(['duplicate', 'odd_rule'])
    argument = random.choice(collatz.theorems)
    collatz.run_rule(rule_name, argument)

Saver.save_game(collatz, 'collatz')
