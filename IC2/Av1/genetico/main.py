import random
import individual as id
Ind = id.Individual
POPULATION_S = 100

gen = 1
found = False

def fitest_of_gen(generation,individual, fit):
    print("Generation:", generation,"\tString:",individual, "\tFitness: ",fit)

def show_gen(population):
    for id in population:
        fitest_of_gen(1,id.chromosome,1)

population = []
for _ in range(POPULATION_S):
    indvidual = Ind.create_genome(Ind)
    population.append(Ind(indvidual))


while not found:
    population = sorted(population, key= lambda id:id.fit)

    if population[0].fit <= 0:
        found = True
        break
    NeX_Gen = []

    slice = int((10*POPULATION_S)/100)
    NeX_Gen.extend(population[:slice])
    slice = int((90*POPULATION_S)/100)
    for _ in range(slice):
        halfs = int((50*POPULATION_S)/100)
        prt1 = random.choice(population[:halfs])
        prt2 = random.choice(population[:halfs])
        child = prt1.mating(prt2)
        NeX_Gen.append(child)
    population = NeX_Gen #So hail NeX Geeeen. This is the end off everything
    gen+=1
    fitest_of_gen(gen,population[0].chromosome,population[0].fit)    
fitest_of_gen(gen,population[0].chromosome,population[0].fit)    
