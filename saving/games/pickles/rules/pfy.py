def pfy(game, theorem_1, theorem_2):
	return theorem_1 + 'p' + theorem_2 if theorem_1 in game.theorems and theorem_2 in game.theorems else False