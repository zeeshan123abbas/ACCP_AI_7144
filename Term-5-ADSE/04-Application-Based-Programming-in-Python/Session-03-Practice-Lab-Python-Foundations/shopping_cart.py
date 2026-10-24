# shopping_cart.py - Lab 2: menu-driven cart (uses while loop + dictionary)
# Run it and type menu numbers. Choose 4 to exit.

prices = {"pen": 50, "notebook": 200, "bag": 1500}   # item -> price
cart = {}                                            # item -> quantity

def show_cart():
    total = 0
    for item, qty in cart.items():
        line_total = prices[item] * qty
        total = total + line_total
        print(f"  {item} x {qty} = Rs {line_total}")
    print(f"  TOTAL = Rs {total}")

while True:
    print("\n1) Show items  2) Add item  3) View cart  4) Exit")
    choice = input("Choose: ")

    if choice == "1":
        for item, price in prices.items():
            print(f"  {item}: Rs {price}")
    elif choice == "2":
        item = input("Item name: ").lower()
        if item in prices:
            qty = int(input("Quantity: "))
            cart[item] = cart.get(item, 0) + qty   # add to existing quantity
            print("Added!")
        else:
            print("Sorry, item not found.")
    elif choice == "3":
        show_cart()
    elif choice == "4":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice, try again.")
