#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))

    if monthly_investment <= 0:
        print("Entry must be greater than 0. Please try again.")
    elif yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        print("Entry must be greater than 0 and less than or equal to 15.","Please try again.")
    elif years <= 0 or years > 50:
        print("Entry must be greater than 0 and less than or equal to 50.","Please try again.")
    else:
        # convert yearly values to monthly values
        monthly_interest_rate = yearly_interest_rate / 12 / 100
        months = years * 12

        # calculate the future value
        future_value = 0
        for i in range(1,months+1):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate
            future_value += monthly_interest_amount

        # display the result
            if i % 12 == 0:
                print("Year = ",i // 12,"\tFuture Value = ",round(future_value,2))        # print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue (y/n)? ")
        print()

print("Bye!")
