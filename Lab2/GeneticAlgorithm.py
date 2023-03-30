import copy
import random
import numpy as np
from cec2017.functions import f1, f2, f3
import matplotlib.pyplot as plt
import Individual

class GeneticAlgorithm:
    def __init__(self):
        self.population=self.generateRandomPopulation()
    def generateRandomPopulation(self):
        population = []
        for i in range(0, 100):  # losowanie populacji
            x = np.random.uniform(-100, 100, size=(1, 10))
            ind = Individual.Individual(x)
            population.append(ind)
        return population

    #pM- probability od mutation [%]
    #tMAX- number of evolution steps
    def geneticAlgorithm(self, pM=5, tMAX=10000):
        POPULATION=len(self.population)
        ELITE = int(POPULATION/2)
        population=self.population
        t=0
        while t<tMAX:
            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            children=[]
            for i in range(ELITE):
                for j in range(int(POPULATION/ELITE)):

                    ind=Individual.Individual(population[i].genes, population[j].score)
                    mutationsCounter=0
                    while 1==1: #draw number of mutations (poisson distibution for p=pM)
                        if random.randint(0,99)<=pM: mutationsCounter+=1
                        else: break
                    while mutationsCounter>1: #make mutations
                        newAllel= random.uniform(-100,100)
                        geneToChange=random.randint(0,9)
                        ind.genes[0][geneToChange]=newAllel
                        mutationsCounter-=1
                    if mutationsCounter==1:
                        newAllel = random.uniform(-100, 100)
                        geneToChange = random.randint(0, 9)
                        ind.genes[0][geneToChange] = newAllel
                        ind.calculateScore()
                    children.append(ind)
            population = children
            t += 1
        self.population=population

    def geneticAlgorithmVerbose(self, pM=5, tMAX=10000):
        POPULATION=len(self.population)
        ELITE = int(POPULATION/2)
        population=self.population
        t=0
        while t<tMAX:
            if t%1000==0:
                print("step: "+ str(t))
                self.printPopulation()
            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            children=[]
            for i in range(ELITE):
                for j in range(int(POPULATION/ELITE)):

                    ind=Individual.Individual(population[i].genes, population[j].score)
                    mutationsCounter=0
                    while 1==1: #draw number of mutations (poisson distibution for p=pM)
                        if random.randint(0,99)<=pM: mutationsCounter+=1
                        else: break
                    while mutationsCounter>1: #make mutations
                        newAllel= random.uniform(-100,100)
                        geneToChange=random.randint(0,9)
                        ind.genes[0][geneToChange]=newAllel
                        mutationsCounter-=1
                    if mutationsCounter==1:
                        newAllel = random.uniform(-100, 100)
                        geneToChange = random.randint(0, 9)
                        ind.genes[0][geneToChange] = newAllel
                        ind.calculateScore()
                    children.append(ind)
            population = children
            t += 1
        self.population=population

    def geneticAlgorithmStats(self, pM=5, tMAX=10000):

        POPULATION=len(self.population)
        ELITE = int(POPULATION/2)
        population=self.population
        bestInd=population[0]
        t=0
        while t<tMAX:
            if t % 200 == 0:
                scoreMean = sum(obj.score for obj in population) / len(population)
                print("step: " + str(t) + " Mean: " + str(scoreMean))

            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            if population[0].score<bestInd.score:
                bestInd = copy.deepcopy(population[0])
                print("New best: "+ str(bestInd) + " current step: "+ str(t))
            children=[]
            for i in range(ELITE):
                for j in range(int(POPULATION/ELITE)):

                    ind=Individual.Individual(population[i].genes, population[j].score)
                    mutationsCounter=0
                    while 1==1: #draw number of mutations (poisson distibution for p=pM)
                        if random.randint(0,99)<=pM:
                            mutationsCounter+=1
                        else: break
                    while mutationsCounter>1: #make mutations
                        newAllel= random.uniform(-100,100)
                        geneToChange=random.randint(0,9)
                        ind.genes[0][geneToChange]=newAllel
                        mutationsCounter-=1
                    if mutationsCounter==1:
                        newAllel = random.uniform(-100, 100)
                        geneToChange = random.randint(0, 9)
                        ind.genes[0][geneToChange] = newAllel
                        ind.calculateScore()
                    children.append(ind)
            population = children
            t += 1
        self.population=population

    def geneticAlgorithm2Stats(self, pM=5, tMAX=10000):
        print(str(pM))
        POPULATION=len(self.population)
        ELITE = int(POPULATION/2)
        population=self.population
        population = sorted(population, key=lambda x: x.score, reverse=False)
        bestInd = copy.deepcopy(population[0])
        t=0
        while t<tMAX:
            if t%200==0:
                scoreMean = sum(obj.score for obj in population) / len(population)
                print("step: "+ str(t)+ " Mean: " + str(scoreMean))
            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            if population[0].score<bestInd.score:
                bestInd = copy.deepcopy(population[0])
                print("New best: "+ str(bestInd) + " current step: "+ str(t))
            children=[]
            for i in range(ELITE):
                for j in range(int(POPULATION/ELITE)):

                    ind=Individual.Individual(population[i].genes, population[j].score)
                    mutationsCounter=0
                    while 1==1: #draw number of mutations (poisson distibution for p=pM)
                        if random.randint(0,99)<=pM:
                            mutationsCounter+=1
                        else: break
                    while mutationsCounter>1: #make mutations
                        change= random.uniform(-10,10)
                        geneToChange=random.randint(0,9)
                        ind.genes[0][geneToChange]+=change
                        mutationsCounter-=1
                    if mutationsCounter==1:
                        change = random.uniform(-10, 10)
                        geneToChange = random.randint(0, 9)
                        ind.genes[0][geneToChange] += change
                        ind.calculateScore()
                    children.append(ind)
            population=children
            t += 1
        self.population=population
    def printPopulation(self):
        for ind in self.population:
            print(ind)

