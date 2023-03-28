class Item:
    def __init__(self, id, price, weight):
        self.id=id
        self.p=price
        self.w=weight
        self.pwratio=price/weight
        self.haveBeenTaken=False

    def __str__(self) -> str:
        return "Id: " + str(self.id) + ", price: " + str(self.p) + ", weight: " + str(self.w) + ", price/weight ratio: " + str(self.pwratio) + ", taken: " + str(self.haveBeenTaken)



