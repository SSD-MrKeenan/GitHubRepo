##age = int(input("How old are you? "))
##years = int(input("How long have you worked here? "))
##
##if age >= 65 or years >= 20:
##    print("Congratulations! You can retire!")
##else:
##    print("Sorry, you must keep working....")

noun = input("Give me a noun: ")
number = int(input("Give me a number: "))

if number > 1:
    print(str(number) + " " + noun + "s")
elif number == 1:
    print(str(number) + " " + noun)
else:
    print("You must enter at least 1.")
