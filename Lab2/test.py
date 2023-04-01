from Lab2.GeneticAlgorithm import GeneticAlgorithm

results=[]
for i in range(25):
    g=GeneticAlgorithm()
    g.generateRandomPopulation(1000)
    bestIndScore=g.geneticAlgorithm(5,10,4,500)
    #bestIndScore=g.geneticAlgorithm2(5,1000)
    results.append(bestIndScore)
mean=sum(results)/len(results)
print(mean)