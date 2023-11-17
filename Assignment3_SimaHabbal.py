items = []
order = []
total = 0
coupons = 0

def main_menu():
    print("Welcome to Aamo El Dekanje!")
    print("1. Start a new order")
    print("2. Close the program")

def order_menu():
    print("\nOrder Menu:")
    print("1. Add a new item to the order")
    print("2. Check the total of the bill")
    print("3. Add a coupon")
    print("4. Checkout")

def add_item():
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input(f"Enter the quantity of {item_name}: "))
    order.append([item_name, item_quantity])
    global total
    total += (item_price * item_quantity)
    print(f"{item_quantity} {item_name}(s) added to the order.")

def check_total():
    print(f"The total of your bill is: ${total:.2f}")

def add_coupon():
    global coupons
    coupon_value = float(input("Enter the coupon value: "))
    coupons += coupon_value
    print(f"${coupon_value:.2f} coupon added to your order.")

def checkout():
    print("\nOrder Summary:")
    for item, quantity in order:
        print(f"{quantity} {item}")
    print(f"Total of the order (without coupons): ${total:.2f}")
    print(f"Total of the coupons: ${coupons:.2f}")
    final_total = total - coupons
    print(f"Total to pay: ${final_total:.2f}")

while True:
    main_menu()
    choice = input("Please select an option (1/2): ")

    if choice == "1":
        order = []
        while True:
            order_menu()
            option = input("Please select an option (1/2/3/4): ")

            if option == "1":
                add_item()
            elif option == "2":
                check_total()
            elif option == "3":
                add_coupon()
            elif option == "4":
                checkout()
                break
            else:
                print("Invalid option. Please try again.")
    elif choice == "2":
        print("Bye bye!")
        break
    else:
        print("Invalid option. Please try again.")
