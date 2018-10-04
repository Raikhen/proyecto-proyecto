def next(game, theorem):
	return 'S' + theorem if theorem in game.theorems else False