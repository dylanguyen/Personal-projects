# Programmer: [Dylan Nguyen]
# Course: CS151, Dr. Simari
# Date: [Feb 12, 2020]
# Programming Assignment: 2
# Program Inputs: [the month in numbers (1-12) and the year]
# Program Outputs: [The amount of days in that specifc month]

# output purpose
print("The purpose of this program is to determine the amount of days in the desired month based on the year.")

# ask the user for the month
month_given= input ("\nPlease enter the desired month numerically. Ex. (1-12):  ")
month_given= int(month_given)

# Ask the user for the month represented in numbers (1-12)
year_given= input("\nPlease enter the full year (Ex. 2020): ")
year_given = int(year_given)

# condition if the month is valid
if month_given < 1 or month_given > 12:

    # output error statement to user
    print("\nError. You have input an invalid number, please input a number between 1 and 12. Please try again. ")

# determine amount of days in month if the month number is valid
else:

    # if month entered is 2, or February check if it is a leap year
    if month_given == 2:

        if year_given % 100 == 0:

            if year_given % 400 == 0:
                days_in_month= 29

            else:
                days_in_month = 28

        elif year_given % 4 == 0:
            days_in_month = 29

        else:
            days_in_month = 28

    elif month_given == 4 or month_given == 6 or month_given == 9 or month_given == 11:
        days_in_month = 30

    else:
        days_in_month = 31

# output result to user
print("\nThe month desired in the year", year_given, "has", days_in_month, "days.")

print("\nThank you for using this program!")