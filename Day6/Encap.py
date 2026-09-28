class Shirt:
    def __init__(self,price):
        self.price=price
    def get_price(self):
        return self.price
    def set_prize(self,price):
        if price>0:
            self.__prize=price
shirt=Shirt(900)
print(shirt.get_price())