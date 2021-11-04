SALES_TAX = .08

def display_menu():
    print("Menu Choices")
    print("--------------------")
    print("1 - Nintendo Switch")
    print("2 - Playstation 5")
    print("3 - XBox One")
    print()
    console = int(input("Please enter 1, 2, or 3: "))
    return console

def display_colors():
    print("Color Choices")
    print("--------------------")
    print("W - White")
    print("B - Black")
    print("S - Silver")
    print()
    color = input("Please enter W, B, or S: ")
    return color

def get_price(console, color):
    color = color.lower()
    
    if console == 1:
        if color == "w":
            price = 300
        elif color == "b":
            price = 315
        elif color == "s":
            price = 350
    elif console == 2:
        if color == "w":
            price = 500
        elif color == "b":
            price = 515
        elif color == "s":
            price = 550
    elif console == 3:
        if color == "w":
            price = 265
        elif color == "b":
            price = 280
        elif color == "s":
            price = 315

    return price

def get_quantity():
    quantity = int(input("How many would you like to purchase? "))
    return quantity

def get_subtotal(quantity, price):
    subtotal = quantity * price
    return subtotal

def get_sales_tax(subtotal):
    tax = subtotal * SALES_TAX
    return tax

def get_total(subtotal, tax):
    total = subtotal + tax
    return total

def display_results(console, color, price, quantity, subtotal, tax, total):
    if console == 1:
        console = "Nintendo Switch"
    elif console == 2:
        console = "Playstation 5"
    elif console == 3:
        console = "XBox One"

    color = color.lower()
    
    if color == "w":
        color = "White"
    elif color == "b":
        color = "Black"
    elif color == "s":
        color = "Silver"
    
    print("Console Purchased: " + console)
    print("Color Choice: " + color)
    print("Cost Per Unit: $" + str(price))
    print("Quantity: " + str(quantity))
    print("--------------------------")
    print("Subtotal: $" + str(subtotal))
    print("Sales Tax: $" + str(round(tax,2)))
    print("--------------------------")
    print("Total Amount: $" + str(total))

def main():
    console = display_menu()
    print()
    color = display_colors()
    price = get_price(console, color)
    print()
    quantity = get_quantity()
    subtotal = get_subtotal(quantity, price)
    tax = get_sales_tax(subtotal)
    total = get_total(subtotal, tax)
    print()
    display_results(console, color, price, quantity, subtotal, tax, total)

if __name__ == "__main__":
    main()
