import GeneticAlgorithm

gn=GeneticAlgorithm.GeneticAlgorithm()
gn.generateRandomPopulation()
gn.geneticAlgorithmStats(50,10000)
gn.printPopulation()