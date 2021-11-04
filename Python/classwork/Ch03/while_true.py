number = 1

while True:
    print(number)
    response = input("Do you want to continue? y/n")

    if response == "y":
        number += 1
    elif response == "n":
        break

print("The loop has ended")
