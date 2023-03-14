import copy

from Lab1.knapsackProblem import Item

class KnapsackProblem:
    def __init__(self, items, maxWeight):
        self.items=items
        self.maxWeight=maxWeight
        self.itemList = self.convert()

    # heuristic sort ralative to p/w and take the best items that fits
    def algorithm1(self):
        self.itemList.sort(key=lambda x: x.pwratio, reverse=True)
        weightSum = 0
        priceSum = 0
        for i in range(0, len(self.itemList)):
            weightSum += self.itemList[i].w
            if weightSum > self.maxWeight: break
            self.itemList[i].haveBeenTaken = True
            priceSum += self.itemList[i].p
        return self.itemList

    #algorithm uses heuristic method but when knapsack is full it take out the worst item and keeps trying to
    #find better solution
    def algorithm2(self):
        self.itemList.sort(key=lambda x: x.pwratio, reverse=True)
        weightSum = 0
        priceSum = 0
        bestItemList = copy.deepcopy(self.itemList)
        bestPriceSum = priceSum
        i = 0
        while 1 == 1:
            # if i points the worst item, we take out this item and second worst item that we have in bag
            if i == len(self.itemList):
                i -= 1
                if self.itemList[i].haveBeenTaken == True:
                    weightSum -= self.itemList[i].w
                    priceSum -= self.itemList[i].p
                    self.itemList[i].haveBeenTaken = False
                while i > 0:
                    i -= 1
                    if self.itemList[i].haveBeenTaken == True:
                        weightSum -= self.itemList[i].w
                        priceSum -= self.itemList[i].p
                        self.itemList[i].haveBeenTaken = False
                        break
                    if i == 0: return bestItemList
                i += 1

            # if we can we add new item
            if weightSum + self.itemList[i].w < self.maxWeight:
                weightSum += self.itemList[i].w
                priceSum += self.itemList[i].p
                self.itemList[i].haveBeenTaken = True

            # check if current bag is better than best bag
            if priceSum > bestPriceSum:
                bestItemList = copy.deepcopy(self.itemList)
                bestPriceSum = priceSum

            # if this condition is true we have optimal solution
            if weightSum == self.maxWeight:
                return bestItemList

            # next item
            i += 1

    #similar to algorithm2 but has steps limit
    def algorithm3(self, maxCounter):
        self.itemList.sort(key=lambda x: x.pwratio, reverse=True)
        weightSum = 0
        priceSum = 0
        bestItemList = copy.deepcopy(self.itemList)
        bestPriceSum = priceSum
        i = 0

        counter = 0

        while 1 == 1:
            # if i points the worst item, we take out this item and second worst item that we have in bag
            if i == len(self.itemList):

                # returns "good enough" solution
                counter += 1
                if counter == maxCounter: return bestItemList

                i -= 1
                if self.itemList[i].haveBeenTaken == True:
                    weightSum -= self.itemList[i].w
                    priceSum -= self.itemList[i].p
                    self.itemList[i].haveBeenTaken = False
                while i > 0:
                    i -= 1
                    if self.itemList[i].haveBeenTaken == True:
                        weightSum -= self.itemList[i].w
                        priceSum -= self.itemList[i].p
                        self.itemList[i].haveBeenTaken = False
                        break
                    if i == 0: return bestItemList
                i += 1

            # if we can we add new item
            if weightSum + self.itemList[i].w < self.maxWeight:
                weightSum += self.itemList[i].w
                priceSum += self.itemList[i].p
                self.itemList[i].haveBeenTaken = True

            # check if current bag is better than best bag
            if priceSum > bestPriceSum:
                bestItemList = copy.deepcopy(self.itemList)
                bestPriceSum = priceSum

            # if this condition is true we have optimal solution
            if weightSum == self.maxWeight:
                return bestItemList

            # next item
            i += 1

    # brute force search O(2^n)
    def algorithm4(self):
        currentWeight = 0
        currentPrice = 0
        bestPrice = 0
        bestItemList = copy.deepcopy(self.itemList)
        for i in range(0, 2 ** len(self.itemList)):
            # set next configuration
            for j in range(0, len(self.itemList)):
                if self.itemList[j].haveBeenTaken == False:
                    currentWeight += self.itemList[j].w
                    currentPrice += self.itemList[j].p
                    self.itemList[j].haveBeenTaken = True
                    break
                self.itemList[j].haveBeenTaken = False
                currentWeight -= self.itemList[j].w
                currentPrice -= self.itemList[j].p

            if currentWeight <= self.maxWeight and currentPrice > bestPrice:
                bestItemList = copy.deepcopy(self.itemList)
                bestPrice = currentPrice
        return bestItemList

    # convert 2dim list "items" to list of Items
    def convert(self):
        itemList = []
        for i in range(0, len(self.items[0])):
            item = Item.Item(i, self.items[0][i], self.items[1][i])
            itemList.append(item)
        return itemList

    def restart(self):
        self.itemList=self.convert()
