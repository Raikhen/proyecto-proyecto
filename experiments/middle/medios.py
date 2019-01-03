'''
How to continue: search for an easier problem. if we only do difficult things, we can't know how complex the things we think should be.
It seems better to trian nns to classify sentences instead of writing them.
'''

import numpy as np
import itertools
from Levenshtein import distance
from middlecito import MiddleTask, one_hot
from time import time

sen_max_length = 60
vocab = ['(', ')', '⇒', ',', '¬', '|', '-']
hidden_size = 50
encoded_size = 50
vocab_size = 7
embed_size = 2
pop_size = 10
mutation_factor = 1
batch_size = 32
middle_task = MiddleTask()
evolution_mode = 'weighted' #"a la dylan"

def main():
    agents = [first_agent() for _ in range(pop_size)]

    for i in itertools.count():
        xs, ys = middle_task.next_batch()
        fitnesses = np.array([evaluate_agent(agent, xs, ys) for agent in agents])
        agents = mutate_and_reproduce(agents, fitnesses)
        print(f'Iteration {i}. Best fitness {np.min(fitnesses)}. Mean fitness {np.mean(fitnesses)}')

def evaluate_agent(agent, xs, ys):
    w_embed, w_xh, w_hh, w_he, w_xe, w_ee, w_eo = agent
    h = np.zeros((batch_size, hidden_size))
    xs = np.swapaxes(xs, 0, 1)

    for x in xs:
        x = [char.dot(w_embed) for char in x]
        x = np.array(x).reshape(batch_size, embed_size * sen_max_length)
        h = np.tanh(np.dot(add_bias(x), w_xh) + np.dot(h, w_hh))

    e = np.dot(add_bias(h), w_he)
    o = {0: np.zeros((batch_size, embed_size))}
    o_letters = [{} for _ in range(batch_size)]

    for i in range(sen_max_length):
        e = np.tanh(np.dot(add_bias(o[i]), w_xe) + np.dot(e, w_ee))
        # o[i] = softmax(w_eo.dot(add_bias(e))) #try: remove softmax
        char_ixs = np.argmin(np.dot(add_bias(e), w_eo), axis=1)
        o[i + 1] = np.array([one_hot(vocab[ix]).dot(w_embed) for ix in char_ixs])
        for batch_i, char_ix in enumerate(char_ixs):
            o_letters[batch_i][i] = vocab[char_ix]

    outputs = [''.join(list(l.values())) for l in o_letters]
    if np.random.randint(20) == 0:
        print(outputs[0], ys[0])
    return np.sum([distance(out, y) for out, y in zip(outputs, ys)]) / batch_size

def first_agent():
    w_embed = np.random.randn(vocab_size, embed_size)
    w_xh = np.random.randn(embed_size * sen_max_length + 1, hidden_size)
    w_hh = np.random.randn(hidden_size, hidden_size)
    w_he = np.random.randn(hidden_size + 1, encoded_size)
    w_xe = np.random.randn(embed_size + 1, encoded_size)
    w_ee = np.random.randn(encoded_size, encoded_size)
    w_eo = np.random.randn(encoded_size + 1, vocab_size)
    return w_embed, w_xh, w_hh, w_he, w_xe, w_ee, w_eo

def mutate_and_reproduce(agents, fitnesses):
    fitnesses = max(fitnesses) - fitnesses
    fitnesses /= sum(fitnesses)
    new_agents = []

    for i in range(pop_size):
        new_agents.append([])
        if evolution_mode == 'weighted':
            agent_i = np.random.choice(range(pop_size), p=fitnesses)
        elif evolution_mode == 'elitism':
            agent_i = np.argmin(fitnesses)
        agent = agents[agent_i]
        for j in range(len(agent)):
            mutated_w = agent[j] + np.random.randn(*agent[j].shape) * mutation_factor
            new_agents[i].append(mutated_w)
    return new_agents

def add_bias(array):
    return np.pad(array, ((0, 0), (0, 1)), 'constant', constant_values=1)

main()
