from fit import single_fit, double_fit
from heapq import heappush, heappop
from tree.functions.to_node         import to_node
from tree.alphabets.logic           import get_logic_alphabet

initial_list = ['⇒(F_0, ⇒(F_1, F_0))', '⇒(⇒(F_0, ⇒(F_1, F_2)), ⇒(⇒(F_0, F_1), ⇒(F_0, F_2)))', '⇒(⇒(¬(F_0), ¬(F_1)), ⇒(F_1, F_0))']
alphabet = get_logic_alphabet()
scorer = Scorer()

def initial_prove(qvq):
	queue = []
	heappush(queue, (1, qvq))

	while len(queue) > 0:
		theorem = heappop(queue)
		if prove(theorem):
			return True

	return False

def prove(qvq, queue):
	fitted = [double_fit(qvq, t) for t in initial_list]
	if any(fitted):
	    return True

	for t in initial_list:
		node = to_node(t, alphabet)
		(left, right), root = node.children, node.symbol.drawing
		if root == '⇒':
			if double_fit(qvq, right):
				heappush(queue, (scorer.score(left), left))

class Scorer:
	def __init__(self):
		self.state = empty
		self.weights = random weights

	def score(self, input):
		# Pasamos el teorema de texto a un vector en (100, 8) dimensiones.
		#  El 100 viene de que usamos theorems de hasta 100 caracteres.
		#  El 8 viene de que usamos 8 caracteres diferentes.
		input = [one_of_k(char) for char in input]
		# Transformamos ambos theorems a otro espacio para hacerlos más compactos y
		#  más fáciles de manejar. (Usamos la misma transformación para ambos.)
		input = self.transform(input)
		# Esta es una abstración de una red neuronal con loops.
		W, U, V = self.weights
		self.state = np.dot(W, input) + np.dot(U, self.state)
		return np.dot(V, self.state)

	@static_method
	def transform(t):
		t = [np.dot(W, char) for char in chars] # Convertimos (100, 8) a (100, 2)
		t = t.flatten() # Convertimos (100, 2) a (200,)
		t = np.dot(U, t) # Convertimos (200,) a (50,)
		return t

	@static_method
	def one_of_k(char):
		return un array de 0s con un 1 en la posición dada por chars[char]
