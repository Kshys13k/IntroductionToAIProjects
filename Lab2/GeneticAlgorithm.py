import copy
import random
import numpy as np
from cec2017.functions import f1, f2, f3
import matplotlib.pyplot as plt
from Lab2.Individual import  Individual

class GeneticAlgorithm:
    def __init__(self):
        self.population=self.generateRandomPopulation(100)
    def generateRandomPopulation(self, populationSize, functionNumber=4):
        population = []
        for i in range(0, populationSize):
            x = np.random.uniform(-100, 100, size=(1, 10))
            ind = Individual(x)
            population.append(ind)
        return population

    #pM- probability od mutation [%]
    #tMAX- number of evolution steps
    def geneticAlgorithmStats(self, pM=5, tMAX=10000, functionNumber=4, elite=50):

        POPULATION=len(self.population)
        population=self.population
        bestInd=population[0]
        t=0
        while t<tMAX:
            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            if population[0].score<bestInd.score:
                bestInd = copy.deepcopy(population[0])
            children=[]
            for i in range(elite):
                for j in range(int(POPULATION/elite)):

                    ind=Individual(population[i].genes, population[j].score)
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
                        ind.calculateScore(functionNumber)
                    children.append(ind)
            population = children
            t += 1
        self.population=population
        return bestInd.score

    def geneticAlgorithmStats(self, pM=5, tMAX=10000, functionNumber=4, elite=50):

        POPULATION=len(self.population)
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
            for i in range(elite):
                for j in range(int(POPULATION/elite)):

                    ind=Individual(population[i].genes, population[j].score)
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
                        ind.calculateScore(functionNumber)
                    children.append(ind)
            population = children
            t += 1
        self.population=population
        return bestInd.score
    def geneticAlgorithm2(self, pM=5, tMAX=10000, functionNumber=4, elite=50):
        print(str(pM))
        POPULATION=len(self.population)
        population=self.population
        population = sorted(population, key=lambda x: x.score, reverse=False)
        bestInd = copy.deepcopy(population[0])
        t=0
        while t<tMAX:
            #choosing elite individuals from population (natural selection) and create new population based on this group (mutations are possible, interbreeding is forbiten)
            population= sorted(population, key=lambda x: x.score, reverse=False)
            if population[0].score<bestInd.score:
                bestInd = copy.deepcopy(population[0])
            children=[]
            for i in range(elite):
                for j in range(int(POPULATION/elite)):

                    ind=Individual(population[i].genes, population[j].score)
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
                        ind.calculateScore(functionNumber)
                    children.append(ind)
            population=children
            t += 1
        self.population=population
        return bestInd.score
    def geneticAlgorithm2Stats(self, pM=5, tMAX=10000, functionNumber=4, elite=50):
        print(str(pM))
        POPULATION=len(self.population)
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
            for i in range(elite):
                for j in range(int(POPULATION/elite)):

                    ind=Individual(population[i].genes, population[j].score)
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
                        ind.calculateScore(functionNumber)
                    children.append(ind)
            population=children
            t += 1
        self.population=population
        return bestInd.score
    def printPopulation(self):
        for ind in self.population:
            print(ind)

