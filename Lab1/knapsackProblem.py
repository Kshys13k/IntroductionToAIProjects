import copy

from Lab1 import Item
#dwuwymiarowa tablica służąca przechowująca informacje o przedmiotach,
#pierwszy rząd-wartość,
#drugi rząd- cena,
#przedmioty oznaczane są przez id od 0 do n, numerowanie od lewej.
items= [[16,8,9,6],
        [8,3,5,2]]

#maksymalna waga= pojemność plecaka
maxWeight=9

#posortowanie względem p/w i wzięcie najkorzystniejszych
def algorithm1():
        itemList.sort(key=lambda x: x.pwratio, reverse=True)
        weightSum=0
        priceSum=0
        for i in range (0,len(itemList)):
            weightSum+=itemList[i].w
            if weightSum>maxWeight: break
            itemList[i].haveBeenTaken=True
            priceSum+=itemList[i].p
        return itemList


#tak jak 1, ale potem przeszukiwanie innych stanów, w obiecującej kolejności
def algorithm2():
    itemList.sort(key=lambda x: x.pwratio, reverse=True)
    weightSum = 0
    priceSum = 0
    bestItemList= copy.deepcopy(itemList)
    bestPriceSum= priceSum
    i=0
    while 1==1:
        #if i points the worst item, we take out this item and second worst item that we have in bag
        if i==len(itemList):
            i-=1
            if itemList[i].haveBeenTaken==True:
                weightSum-=itemList[i].w
                priceSum-=itemList[i].p
                itemList[i].haveBeenTaken=False
            while i>0:
                i-=1
                if itemList[i].haveBeenTaken==True:
                    weightSum -= itemList[i].w
                    priceSum -= itemList[i].p
                    itemList[i].haveBeenTaken = False
                    break
                if i==0: return bestItemList
            i+=1

        #if we can we add new item
        if weightSum + itemList[i].w < maxWeight:
            weightSum += itemList[i].w
            priceSum += itemList[i].p
            itemList[i].haveBeenTaken=True

        #check if current bag is better than best bag
        if priceSum>bestPriceSum:
            bestItemList=copy.deepcopy(itemList)
            bestPriceSum=priceSum

        #if this condition is true we have optimal solution
        if weightSum==maxWeight:
            return bestItemList

        #next item
        i+=1

def algorithm3(maxCounter):
    itemList.sort(key=lambda x: x.pwratio, reverse=True)
    weightSum = 0
    priceSum = 0
    bestItemList= copy.deepcopy(itemList)
    bestPriceSum= priceSum
    i=0

    counter=0

    while 1==1:
        #if i points the worst item, we take out this item and second worst item that we have in bag
        if i==len(itemList):

            #returns "good enough" solution
            counter+=1
            if counter==maxCounter: return bestItemList

            i-=1
            if itemList[i].haveBeenTaken==True:
                weightSum-=itemList[i].w
                priceSum-=itemList[i].p
                itemList[i].haveBeenTaken=False
            while i>0:
                i-=1
                if itemList[i].haveBeenTaken==True:
                    weightSum -= itemList[i].w
                    priceSum -= itemList[i].p
                    itemList[i].haveBeenTaken = False
                    break
                if i==0: return bestItemList
            i+=1

        #if we can we add new item
        if weightSum + itemList[i].w < maxWeight:
            weightSum += itemList[i].w
            priceSum += itemList[i].p
            itemList[i].haveBeenTaken=True

        #check if current bag is better than best bag
        if priceSum>bestPriceSum:
            bestItemList=copy.deepcopy(itemList)
            bestPriceSum=priceSum

        #if this condition is true we have optimal solution
        if weightSum==maxWeight:
            return bestItemList

        #next item
        i+=1





itemList=[]
for i in range (0,len(items[0])):
        item=Item.Item(i,items[0][i],items[1][i])
        itemList.append(item)
result=algorithm2()
for i in range (0, len(result)):
            print(result[i])

