import numpy as np
import random
import math

# Define parameters
CITIES = 15
GRID_SIZE = 5
POPULATION_SIZE = 45
NUM_GENERATIONS = 50
MUTATION_PROBABILITY = 0.1

# Generate random points (cities)
cities = set()
while len(cities) < CITIES:
    x = round(random.uniform(0, GRID_SIZE), 2)
    y = round(random.uniform(0, GRID_SIZE), 2)
    cities.add((x, y))

# Define helper function to calculate distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize population
population = []
for _ in range(POPULATION_SIZE):
    individual = list(cities)
    random.shuffle(individual)
    population.append(individual)

# Define fitness function
def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distance(individual[i], individual[i + 1])
    total_distance += distance(individual[-1], individual[0])  # distance back to starting city
    return total_distance

# Genetic Algorithm main loop
for generation in range(NUM_GENERATIONS):
    # Evaluate fitness of each individual
    fitness_scores = [(individual, calculate_fitness(individual)) for individual in population]
    # Sort population based on fitness
    sorted_population = sorted(fitness_scores, key=lambda x: x[1])
    # Select the best individual
    best_individual, best_fitness = sorted_population[0]
    # Print best individual and its fitness value for each generation
    print(f"Generation {generation + 1}: Best Individual: {best_individual}, Fitness: {best_fitness}")
    # Apply tournament selection to choose parents for crossover
    selected_parents = random.sample(sorted_population, k=2)
    parent1, _ = min(selected_parents, key=lambda x: x[1])
    selected_parents = random.sample(sorted_population, k=2)
    parent2, _ = min(selected_parents, key=lambda x: x[1])
    # Order Crossover (OX) to create offspring
    start, end = sorted(random.sample(range(CITIES), k=2))
    offspring1 = parent1[start:end] + [city for city in parent2 if city not in parent1[start:end]]
    offspring2 = parent2[start:end] + [city for city in parent1 if city not in parent2[start:end]]
    # Perform Swap Mutation on offspring
    if random.random() < MUTATION_PROBABILITY:
        idx1, idx2 = random.sample(range(CITIES), k=2)
        offspring1[idx1], offspring1[idx2] = offspring1[idx2], offspring1[idx1]
        idx1, idx2 = random.sample(range(CITIES), k=2)
        offspring2[idx1], offspring2[idx2] = offspring2[idx2], offspring2[idx1]
    # Replace old population with new population
    population = [offspring1, offspring2] + [individual for individual, _ in sorted_population[2:]]

# Output final best individual found
print("\nFinal Best Individual:", best_individual)
print("Fitness:", best_fitness)
