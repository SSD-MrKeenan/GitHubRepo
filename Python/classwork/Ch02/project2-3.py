print("Tip Calculator")
print()

mealCost = float(input("Cost of the meal: "))
tipPercent = float(input("Tip percent: "))

tipDecimal = tipPercent / 100
tipTotal = round(mealCost * tipDecimal,2)
mealTotal = round(mealCost + tipTotal,2)

print("Tip total: " + str(tipTotal))
print("Total amount: " + str(mealTotal))
