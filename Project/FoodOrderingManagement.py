'''Food Ordering Management 
1. View Menu
2. Add Item
3. Remove Item
4. View Cart
5. Calculate Bill
6. Place Order
7. Order History
8. Exit
'''
from datetime import date
import json
from streamlit import status 
orders=[]
menu=[]
cart=[]
def save_data():
    with open("orders.json","w") as f:
        json.dump(orders,f)
def load_data():
    global orders
    try:
        with open("orders.json","r") as f:
            orders=json.load(f)
    except FileNotFoundError:
        orders=[]
def view_menu():
    if len(menu) == 0:
        print("No Food Items!")
    else:
        for item in menu:
            print("Item ID: ",item["id"])
            print("Food Name: ",item["name"])
            print("Price: ",item["price"])
def add_item():
    item_id=int(input("Enter Item ID: "))
    item_name=input("Enter Item names: ")
    item_price=float(input("Enter price: "))
    item_quantity=int(input("Enter Quantity: "))
    total = item_price * item_quantity
    order={
        "id": item_id,
        "name": item_name,
        "price": item_price,
        "quantity": item_quantity,
        "total": total,
    }
    menu.append(order)
    save_data()
    print("Item Added Successfully!")
def add_item_cart():
    if len(menu)==0:
        print("Menu Empty!")
        return
    view_menu()
    item_id=int(input("Enter Item ID: "))
    quantity=int(input("Enter Quantity: "))
    for item in menu:
        if item["id"] == item_id: 
            total = item["price"] * quantity 
            cart_item = { 
                "id": item["id"], 
                "name": item["name"], 
                "price": item["price"], 
                "quantity": quantity, 
                "total": total 
                } 
            cart.append(cart_item) 
            print("Item Added to Cart Successfully!") 
            return 
    print("Food Item Not Found!")


def remove_item():
    if len(cart)==0:
        print("Cart is Empty!")
        return
    food_name = input("Enter food name to remove:")
    for item in cart:
        if item["name"].lower() == food_name.lower():
            cart.remove(item)
            print("Food item removed successfully!")
            return
    print("Food item not found!")
def view_cart():
    if len(cart) == 0:
        print("Cart is Empty!")
        return
    for item in cart:
        print("Food:", item["name"])
        print("Price:", item["price"])
        print("Quantity:", item["quantity"])
        print("Total:", item["total"])
def calculate_bill():
    if len(cart) == 0:
        print("cart is Empty!")
        return
    total = 0
    for item in cart:
        total=total + item["total"]
    print("Total Bill: ",total)
def place_order():
    if len(cart) == 0:
        print("Cart is empty!")
        return
    total = 0
    for item in cart:
        total = total + item["total"]
    order = {
        "items": cart.copy(),
        "total": total
    }
    orders.append(order)
    cart.clear()
    save_data()
    print("Order placed successfully!")
def order_history():
    if len(orders) == 0:
        print("No order history found.")
        return
    order_number = 1
    for order in orders:
        print("Order:", order_number)
        for item in order["items"]:
            print("Food:", item["name"])
            print("Price:", item["price"])
            print("Quantity:", item["quantity"])
            print("Total:", item["total"])
        print("Order Total:", order["total"])
        order_number = order_number + 1
def main():
    load_data()
    while True:
        print("\nFood Ordering Management:")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Add Item To Cart")
        print("4. Remove Item")
        print("5. View Cart")
        print("6. Calculate Bill")
        print("7. Place Order")
        print("8. Order History")
        print("9. Exit")
        choice = input("Enter your choice (1-8):")
        if choice == "1":
            view_menu()
        elif choice == "2":
            add_item()
        elif choice == "3":
            add_item_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            view_cart()
        elif choice == "6":
            calculate_bill()
        elif choice == "7":
            place_order()
        elif choice == "8":
            order_history()
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()


