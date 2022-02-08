import random
from random import randint
from datetime import datetime


class Knapsack:

    # Iinitialiser les attributs
    def __init__(self, objets, capacity, nb_generation):
        self.objets = objets
        self.capacity = capacity
        self.population = []
        self.nb_generation = nb_generation
        self.meilleures = []

    # Créer population initiale
    def initiale_population(self):
        for item in range(len(self.objets) + len(self.objets)):
            individu = []
            for i in range(len(self.objets)):
                individu.append(randint(0, 1))
            self.population.append(individu)

    # Calculer fitness
    def fitness(self, individu):
        fitness = 0
        poids = 0
        for i, j in enumerate(individu):
            if j == 1:
                fitness += objets[i][1]
                poids += objets[i][2]
        if poids > capacity:
            return 0
        return fitness

    def selection(self, pop):
        sort_pop = sorted(pop)
        new_pop = sort_pop[-2:]
        sort_pop.pop(-1)
        sort_pop.pop(-2)
        new_pop.append(sort_pop[randint(0, 1)])
        new_pop.append(sort_pop[randint(0, 1)])
        return new_pop

    def crossover(self, pop):
        new_pop = []
        cross_param = len(objets)//2
        cross_param = random.choice([cross_param, cross_param-1, cross_param+1])
        i1 = pop[0]
        i2 = pop[1]
        i3 = pop[2]
        i4 = pop[3]

        new_1 = [i1[1][i] for i in range(len(i1[1])-cross_param)]
        new_1 += [i2[1][i] for i in range(len(i2[1])-cross_param, len(i3[1]))]
        new_1 = (self.fitness(new_1), new_1)

        new_2 = [i2[1][i] for i in range(len(i2[1])-cross_param)]
        new_2 += [i1[1][i] for i in range(len(i1[1])-cross_param, len(i1[1]))]
        new_2 = (self.fitness(new_2), new_2)

        new_3 = [i3[1][i] for i in range(len(i3[1])-cross_param)]
        new_3 += [i4[1][i] for i in range(len(i4[1])-cross_param, len(i3[1]))]
        new_3 = (self.fitness(new_3), new_3)

        new_4 = [i4[1][i] for i in range(len(i4[1])-cross_param)]
        new_4 += [i3[1][i] for i in range(len(i3[1])-cross_param, len(i3[1]))]
        new_4 = (self.fitness(new_4), new_4)

        new_pop.append(new_1)
        new_pop.append(new_2)
        new_pop.append(new_3)
        new_pop.append(new_4)

        return new_pop

    def mutation(self, pop):
        i = randint(0, len(pop)-1)
        j = randint(0, len(pop)-1)
        gene = pop[i][1][j]

        if gene == 0:
            pop[i][1][j] = 1
            pop[i] = (self.fitness(pop[i][1]), pop[i][1])
        else:
            pop[i][1][j] = 0
            pop[i] = (self.fitness(pop[i][1]), pop[i][1])

        return pop

    def generation_suivante(self, pop):

        # Ajouter le meilleure dans les list des meilleures
        if sorted(pop)[-1:] not in self.meilleures:
            self.meilleures.append(sorted(pop)[-1:])


        # formaliser la population
        pop = [pop[i][1] for i in range(len(pop))]
        sort_pop = sorted(pop)
        new_pop = sort_pop[-2:]
        for item in range(2):
            individu = []
            for i in range(len(self.objets)):
                individu.append(randint(0, 1))
            new_pop.append(individu)
        self.population = new_pop

    def executor(self):
        self.initiale_population()
        print("-----Population initiale-------")
        print(self.population)

        print("-------------------------------------------------")

        for i in range(self.nb_generation+1):

            print(f"\n----Generation no {i+1}")
            fitness = []
            for i in self.population:
                fitness.append(self.fitness(i))

            pop_fitness = []

            for i in range(len(self.population)):
                pop_fitness.append((fitness[i], self.population[i]))

            print("-----Fitness--------")
            print(pop_fitness)

            pop_selection = self.selection(pop_fitness)
            print("-----Selection---------")
            print(pop_selection)

            pop_cross = self.crossover(pop_selection)
            print("-----Crosse over-------")
            print(pop_cross)

            pop_mutation = self.mutation(pop_cross)
            print("-----Mutation-------")
            print(pop_mutation)
            self.generation_suivante(pop_mutation)

        print(f"\nMeilleures sol ---> {sorted(self.meilleures, reverse=True)}")
        print(f"l'opt de ces generations est {sorted(self.meilleures, reverse=True)[0]}")


START_TIME = datetime.now()

#         ('nom',value,poids)
objets = (('obj 1', 12, 10), ('obj 2', 8, 3), ('obj 3', 7, 11), ('obj 4', 17, 13))
# objets = (('obj 1', 12, 10), ('obj 2', 8, 3), ('obj 3', 7, 11), ('obj 4', 17, 13), ('obj 4', 9, 10))
# objets = (('obj 1', 12, 10), ('obj 2', 8, 3), ('obj 3', 7, 11), ('obj 4', 17, 13), ('obj 4', 9, 10), ('obj5', 10, 10))
capacity = 23
nb_generation = 10

k = Knapsack(objets, capacity, nb_generation)

k.executor()
END_TIME = datetime.now()
print("Temp d'execution -->", END_TIME-START_TIME)
