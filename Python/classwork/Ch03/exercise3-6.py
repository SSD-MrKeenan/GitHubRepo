print("Menu Choices")
print("====================")
print("1 - Nintendo Switch")
print("2 - Playstation 5" )
print("3 - Xbox One" )
system = int(input("Please enter 1, 2, or 3: "))
print()

print("Color Choices")
print("====================")
print("W - White")
print("B - Black")
print("S - Silver")
color = input("Please enter W, B, or S: ")
print()

qty = int(input("How many units would you like to buy? "))
print()

if system == 1:
    systemName = "Nintendo Switch"
    if color.lower() == "w":
        price = 300
    elif color.lower() == "b":
        price = 315
    elif color.lower() == "s":
        price = 350
elif system == 2:
    systemName = "Playstation 5"
    if color.lower() == "w":
        price = 500
    elif color.lower() == "b":
        price = 515
    elif color.lower() == "s":
        price = 550
elif system == 3:
    systemName = "XBox One"
    if color.lower() == "w":
        price = 265
    elif color.lower() == "b":
        price = 280
    elif color.lower() == "s":
        price = 315
        
if color.lower() == "w":
    colorName = "White"
elif color.lower() == "b":
    colorName = "Black"
elif color.lower() == "s":
    colorName = "Silver"
    
total = qty * price
    
print("Game System:\t" + str(systemName))
print("Color:\t\t" + str(colorName))
print("Quantity:\t" + str(qty))
print("Total:\t\t" + str(total))
