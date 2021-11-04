cents = int(input("Enter amount: "))

# assume starting with 99 cents

quarters = cents // 25 # results in 3
cents = cents % 25 # result in 24

dimes = cents // 10 # result in 2
cents = cents % 10 # result in 4

nickels = cents // 5 # result in 0
cents = cents % 5 # result in 0

pennies = cents // 1 # result in 4
cents = cents% 1 # result in 0

print(quarters)
print(dimes)
print(nickels)
print(pennies)
