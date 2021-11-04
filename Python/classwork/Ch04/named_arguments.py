##def calculate(miles,gallons = 15):
##    mpg = miles / gallons
##    return mpg
##
##
##def main():
##    miles = int(input("How many miles did you travel? "))
##    gallons = int(input("How many gallons of gas did you use? "))
##
##    mpg = calculate(miles,gallons)
##
##    print("Your crummy car only gets",mpg,"miles per gallon!")

def generate(f,l,c,d):
    username = f + l + str(d) + c
    return username

def main():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    favorite_color = input("What is your favorite color? ")
    three_digits = int(input("Give me 3 digits: "))
    
    username = generate(d=three_digits,f=first_name,c=favorite_color,l=last_name)

    print("Your new username is: " + username)


if __name__ == "__main__":
    main()
