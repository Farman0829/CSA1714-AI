import random

def fitness(ch):
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(ch[i] - ch[j]) == abs(i - j):
                attacks += 1
    return 28 - attacks

def crossover(p1, p2):
    a, b = sorted(random.sample(range(8), 2))
    child = [-1] * 8
    child[a:b+1] = p1[a:b+1]

    values = [x for x in p2 if x not in child]
    k = 0

    for i in list(range(b+1, 8)) + list(range(a)):
        child[i] = values[k]
        k += 1

    return child

def mutation(child):
    if random.random() < 0.2:
        i, j = random.sample(range(8), 2)
        child[i], child[j] = child[j], child[i]
        return True
    return False

random.seed(10)

population = [random.sample(range(8), 8) for _ in range(100)]

print("Initial Chromosome:", population[0])
print("Initial Fitness:", fitness(population[0]))

for generation in range(1, 1001):
    population.sort(key=fitness, reverse=True)

    if fitness(population[0]) == 28:
        print("\nSolution Found!")
        print("Generation:", generation)
        print("Chromosome:", population[0])
        print("Fitness Value:", fitness(population[0]))
        break

    new_population = population[:2]

    while len(new_population) < 100:
        p1 = max(random.sample(population, 3), key=fitness)
        p2 = max(random.sample(population, 3), key=fitness)

        child = crossover(p1, p2)
        mutated = mutation(child)

        if len(new_population) == 2:
            print("\nCrossover Parent 1:", p1)
            print("Crossover Parent 2:", p2)
            print("Offspring:", child)
            print("Mutation:", "Applied" if mutated else "Not Applied")

        new_population.append(child)

    population = new_population
