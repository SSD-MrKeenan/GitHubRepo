print("Seat Location\t\tPrice per ticket")
print("Box\t\t\t75")
print("Pavilion\t\t30")
print("Lawn\t\t\t21")
print()
location = input("Where would you like to sit? ")
quantity = int(input("How many seats do you want? "))       
ticket_price = 0

if location.lower() == "box":
    ticket_price = 75
elif location.lower() == "pavilion":
    ticket_price = 30
elif location.lower() == "lawn":
    ticket_price = 21
else:
    error = "yes"


if error == "yes":
    print("Sorry, that location is not available")
else:
    total_cost = ticket_price * quantity

    print("Seat Location: " + location)
    print("Price per ticket: " + str(ticket_price))
    print("Quantity ordered: " + str(quantity))
    print("----------------------------------")
    print("Total amount due: " + str(total_cost))

