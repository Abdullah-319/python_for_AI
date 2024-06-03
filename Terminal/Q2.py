import random

targetValue = 60 # here i defined static variables
errorCapacity = 3

# here i defined a function to calculate the fitness based on given equation
def checkFitness(p, q):
    return abs(4*p + 3*q - targetValue)

# here i'm generating random initial population
def populationInitialize(population_size):
    return [(random.randint(0, targetValue), random.randint(0, targetValue)) for _ in range(population_size)]

# i'm  to performing crossover to ombine genes of parents to create children
def doCrossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# here i wrote a function to perform mutation to randomly alter some children
def doMutation(individual):
    mutation_point = random.randint(0, len(individual) - 1)
    mutated_value = random.randint(0, targetValue)
    return individual[:mutation_point] + (mutated_value,) + individual[mutation_point + 1:]

# this is the main genetic algo
def geneticAlgorithm(populationSize, generationsCount):
    population = populationInitialize(populationSize)
    for _ in range(generationsCount):
        # evaluated fitness for each person
        fitnessArray = [checkFitness(p, q) for p, q in population]
        # here i checked for convergence
        if any(score <= errorCapacity for score in fitnessArray):
            reqindex = fitnessArray.index(min(fitnessArray))
            return population[reqindex]
        # here parents are selected to do crossover
        parents = [population[i] for i in range(populationSize) if random.random() < 0.5]
        # here i created new generation by mutation and crossover and stored them in an array
        nextGeneration = []
        while len(nextGeneration) < populationSize:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child1, child2 = doCrossover(parent1, parent2)
            child1 = doMutation(child1)
            child2 = doMutation(child2)
            nextGeneration.extend([child1, child2])
        population = nextGeneration

# here i wrote a random function to test the algo
def run_genetic_algorithm():
    answer = geneticAlgorithm(populationSize=75, generationsCount=500)
    print("Best solution (p, q):", answer)

# here i called the function to run the genetic algo
run_genetic_algorithm()
