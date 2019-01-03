'''
next steps: simplify the code as much as possible. try to understand what we are doing. the current bug seems to be that we are wrongly calculating the weighted mutation, because it's negative when it can't be negative.
#todo: plot mutations distribution
try using different improvmenet functions
we can also try fitting the variance.
'''
import time
import random
import numpy as np

b = .2
pop_size = 100
dims = 1
clip = 10
mean = 0

error = lambda x: (x - 100) ** 2
normal = lambda mean: np.random.randn() + mean

def execute():
    errors = np.array([error(x) for x in agents])
    return np.expand_dims(errors, 1)

def mutate(prev_mutations, prev_errors, errors):
    global mean
    if np.sum(prev_errors) != 0:
        print (errors[:10], prev_errors[:10])
        improvement = 1 - errors / prev_errors
        weighted_mutations = prev_mutations * improvement
        weighted_mutations = np.clip(np.mean(weighted_mutations), -clip, clip)
        print(weighted_mutations, mean, improvement[:10], prev_mutations[:10])
        mean = weighted_mutations + mean

    mutations = np.zeros((pop_size, dims))
    # mean = 0

    for i, x in enumerate(agents[:-1]):
        x_delta = normal(mean)
        mutations[i] = x_delta
        agents[i] = x + x_delta

    return mutations

agents = np.random.randn(pop_size, dims)
prev_errors, errors = np.zeros((2, pop_size, 1))
prev_mutations = np.zeros((pop_size, dims))
error_acc = {}

for i in range(10):
    mutations = mutate(prev_mutations, prev_errors, errors)
    prev_errors, prev_mutations = errors, mutations
    errors = execute()

    best_agent = np.argmin(errors)
    agents = [agents[best_agent] for _ in agents]

    rand_agent = random.choice(agents)
    #rand_agent = int(rand_agent[0]), int(rand_agent[1])
    print(f'{i}) Random agent: {rand_agent}. Error: {error(rand_agent)}. Mean {mean}')
    error_acc[i] = np.mean([error(agent) for agent in agents])
    time.sleep(1e-3)
    # plot(error_acc)
