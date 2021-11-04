print("Time Travel Calculator")
print()

miles = float(input("How many miles did you drive? "))
mph = int(input("How fast were you going? "))

hours = miles // mph
minutes = miles % mph

print("Estimated travel time")
print("Hours: " + str(hours))
print("Minutes: " + str(minutes))
