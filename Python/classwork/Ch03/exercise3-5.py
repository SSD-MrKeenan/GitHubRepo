banknote = int(input("Give me a banknote value: "))

if banknote == 1:
    person = "George Washington"
elif banknote == 2:
    person = "Thomas Jefferson"
elif banknote == 5:
    person = "Abraham Lincoln"
elif banknote == 10:
    person = "Alexander Hamilton"
elif banknote == 20:
    person = "Andrew Jackson"
elif banknote == 50:
    person = "Ulysses S. Grant"
elif banknote == 100:
    person = "Benjamin Franklin"
else:
    person = "No one"

print(person + " is on the " + str(banknote) + " dollar bill.")
