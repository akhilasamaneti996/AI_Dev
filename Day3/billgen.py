print("=====GENZ BILL GENERATOR=====")
item_name=input("Enter the name: ")
item_price=float(input("Enter item price: "))
quantity=int(input("Enter quantity: "))
tax_percent=float(input("Enter tax percentage: "))
total_price=item_price * quantity
tax_amount=total_price * tax_percent/100
final_amount=total_price+tax_amount
print("\n=====BILL DETAILS=====")
print("Item Name: ",item_name)
print("Item Price: $",item_price)
print("Quantity: $",quantity)
print("Total Price: $",total_price)
print("Tax Amount: $",tax_amount)
print("Final Amount: $",final_amount)

