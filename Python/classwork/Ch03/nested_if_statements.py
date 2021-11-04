##gasType = input("What type of gas did you purchase? ")
##gallons = int(input("How many gallons did you purchase? "))
##
##if gasType.lower() == "regular":
##    pricePerGallon = 2.89
##elif gasType.lower() == "super":
##    pricePerGallon = 3.09
##elif gasType.lower() == "premium":
##    pricePerGallon = 3.29
##
##cost = round(gallons * pricePerGallon,2)
##
##print("You spent $" + str(cost) + " on " + str(gallons) + " gallons of " + gasType + " gas.")


genre = input("What genre do you want? ")
show = input("What show do you want? ")

if genre.lower() == "action":
    
    if show.lower() == "vikings":
        channel = 12
    elif show.lower() == "arrow":
        channel = 14
    elif show.lower() == "daredevil":
        channel = 18
        
elif genre.lower() == "kids":
    
    if show.lower() == "octonauts":
        channel = 2
    elif show.lower() == "oswald":
        channel = 4
    elif show.lower() == "arthur":
        channel = 5
        
elif genre.lower() == "comedy":
    
    if show.lower() == "community":
        channel = 30
    elif show.lower() == "seinfeld":
        channel = 35
    elif show.lower() == "friends":
        channel = 39
        
elif genre.lower() == "sports":
    
    if show.lower() == "baseball":
        channel = 21
    elif show.lower() == "football":
        channel = 25
    elif show.lower() == "basketball":
        channel = 27
    elif show.lower() == "soccer":
        channel = 29

print(show + " is on channel " + str(channel))
