print("=====RESTAURANT BILL GENERATOR=====")
n=int(input("Enter number of items: "))
subtotal=0
for i in range(n):
    print("\nEnter details for item", i+1)
    item_name=input("Enter item name: ")
    item_price=float(input("Enter item price: "))
    quantity=int(input("Enter quantity: "))
    item_total=item_price*quantity
    subtotal+=item_total

tax_percent=float(input("\nEnter tax percentage: "))
tax_amount=subtotal*tax_percent/100
final_amount=subtotal+tax_amount

service_charge_percent=float(input("\nEnter service charge percentage: "))
service_charge_amount=subtotal*service_charge_percent/100
final_amount+=service_charge_amount
print("\n=====BILL DETAILS=====")
print("Subtotal: $", subtotal)
print("Tax Amount: $", tax_amount)
print("Service Charge Amount: $", service_charge_amount)
print("Final Amount: $", final_amount)

remove_service_charge=input("\nDo you want to remove service charge? (yes/no): ")
if remove_service_charge.lower()=="yes":
    final_amount-=service_charge_amount
    print("\nService charge removed.")
    print("Final Amount after removing service charge: $", final_amount)
else:
    print("\n===FINAL BILL=======")
    print("Subtotal: $", subtotal)
    print("Tax Amount: $", tax_amount)
    print("Service Charge Amount: $", service_charge_amount)
    print("Final Amount: $", final_amount)