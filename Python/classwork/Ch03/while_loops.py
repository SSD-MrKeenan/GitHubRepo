##count = 1
##
##while count < 9:
##    print("The count is",count)
##    count += 1


##choice = "y"
##
##while choice.lower() == "y":
##    print("Hello!")
##    choice = input("Say hello again? (y/n): ")
##print("Bye!")

##count = 1
##
##while count < 9:
##    if count == 5:
##        break
##    print("The count is",count)
##    count += 1

count = 1

while count < 9:
    if count == 5:
        print("We have reached 5")
        count += 1
        continue
    print("The count is",count)
    count += 1
