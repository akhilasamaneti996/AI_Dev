class Shirt:
    def wear(self):
        print("Wearing nrml shirt")
class FormalShirt(Shirt):
    def wear(self):
        print("Wearing formal shirt")
class Tshirt(Shirt):
    def wear(self):
        print("Wearing tshirt")
shirts=[FormalShirt(),Tshirt()]
for shirt in shirts:
    shirt.wear()