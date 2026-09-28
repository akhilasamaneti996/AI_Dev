def Shirtstore():
    def buy_shirt(self):
        self.__check_inventory()
        self.__process_payment()
        print("Shirt purchased")
    def check_inventory(self):
        print("Checking inventory")
    def process_payment(self):
        print("Processing payment")
store=Shirtstore()
store.check_inventory()



