import random

def fitness(x):
    return x ** 2

population = [random.randint(0, 31) for _ in range(6)]

generations = 20
mutation_rate = 0.1

for generation in range(generations):

    
    population.sort(key=fitness, reverse=True)

    
    parents = population[:3]

    
    offspring = []
    for i in range(3):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        child = (parent1 + parent2) // 2
        offspring.append(child)

    
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = random.randint(0, 31)

    
    population = parents + offspring

    
    best = max(population, key=fitness)

    print("Generation:", generation + 1,
          "Best Solution:", best,
          "Fitness:", fitness(best))


best = max(population, key=fitness)

print("\nOptimal Solution:", best)
print("Maximum Fitness:", fitness(best))
