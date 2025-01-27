print("******* Welcome to our TASTY CORNER ******")
menu = input("Would you like Veg or Non-Veg? ")
veg = {
    "Dosa": 50, "Paneer Tikka": 120, "Chole Bhature": 100, "Nool Parotta": 80,
    "Kizhi Parotta": 150, "Biriyani": 200, "Noodles": 90, "Fried Rice": 110
}
non_veg = {
    "Fish Curry": 250, "Grilled Fish": 300, "Fish Fry": 280, "Mutton Biryani": 350,
    "Butter Chicken": 220, "Chicken 65": 180, "Chicken Biryani": 250
}
gst_rate = 0.05  
total_price = 0  
ordered_items = {}  
deliver = input("Do you want to deliver the food? (yes or no): ")
delivery_charge = 0  
if deliver == "yes":
    address = input("Enter your address: ")
    print(f"Your order will be delivered to: {address}")
else:
    print("Your order will be ready for pickup in 30 minutes.")
if menu == "veg":
    print("\nVeg Menu with Prices:")
    for dish, price in veg.items():
        print(f"{dish}: ₹{price}")
    while True:
        order = input("\nEnter the dish you want to order (or type 'done' to finish): ")
        if order.lower() == "done":
            break            
        if order in veg:
            quantity = input(f"How many plates of {order} would you like? ")
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                price = veg[order] * quantity
                gst = price * gst_rate
                total_price += price + gst
                ordered_items[order] = ordered_items.get(order, 0) + quantity
                print(f"You have ordered {quantity} plates of {order}. Price: ₹{veg[order]} each, Total: ₹{price}, GST: ₹{gst:.2f}, Final: ₹{price + gst:.2f}. Enjoy your meal!")
            else:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Sorry, this dish is not available in our Veg Menu.")
elif menu == "non-veg":
    print("\nNon-Veg Menu with Prices:")
    for dish, price in non_veg.items():
        print(f"{dish}: ₹{price}")
    while True:
        order = input("\nEnter the dish you want to order (or type 'done' to finish): ")
        if order.lower() == "done":
            break
        if order in non_veg:
            quantity = input(f"How many plates of {order} would you like? ")
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                price = non_veg[order] * quantity
                gst = price * gst_rate
                total_price += price + gst
                ordered_items[order] = ordered_items.get(order, 0) + quantity
                print(f"You have ordered {quantity} plates of {order}. Price: ₹{non_veg[order]} each, Total: ₹{price}, GST: ₹{gst:.2f}, Final: ₹{price + gst:.2f}. Enjoy your meal!")
            else:
                print("Invalid quantity. Please enter a valid number.")
        else:
           print("Sorry, this dish is not available in our Non-Veg Menu.")
else:
    print("Sorry, we only serve Veg and Non-Veg dishes. Please choose from the menu.")                          
if len(ordered_items) > 2 and deliver == "yes":
    delivery_charge = 100
    total_price += delivery_charge
if total_price > 0:    
    print("\n******* FINAL BILL *******")
    print("Items Ordered:")
    for dish, qty in ordered_items.items():
        print(f"{dish} - {qty} plates")
    subtotal = total_price - (delivery_charge if deliver == "yes" else 0)
    print(f"\nSubtotal (including GST): ₹{subtotal:.2f}")
    if delivery_charge > 0:
        print(f"Delivery Charge: ₹{delivery_charge}")
    print(f"\nTotal Amount (including GST & Delivery): ₹{total_price:.2f}")
    print("Thank you for ordering from TASTY CORNER!") 
    print("offers are available for you in the TASTY CORNER! offers  starts from  1/2/2025 to 25/2/2025")
