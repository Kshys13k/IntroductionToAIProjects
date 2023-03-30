import GeneticAlgorithm

gn=GeneticAlgorithm.GeneticAlgorithm()
gn.generateRandomPopulation(1000)
gn.geneticAlgorithmStats(5,1000)
gn.printPopulation()