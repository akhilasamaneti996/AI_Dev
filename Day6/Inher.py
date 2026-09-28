class Shirt:
    def wear(self):
        print("Wearing Shirt")
class FormalShirt(Shirt):
    def office(self):
        print("Suitable for office")
shirt=FormalShirt()
shirt.wear()
shirt.office()