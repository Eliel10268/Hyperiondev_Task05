
# i imported math module to use for compound interest calculation
import math

#this will be displayed on the screen as a welcome message and for user to select the options
print("Welcome to the Finance Calculator!")
print("What would you like to calculate?")
print("1: Investment - to calculate the amount of interest you will earn on your investment")
print("2: Bond - to calculate the amount you will have to pay on a home loan")

#the user will enter their choices and input will be converted into lowercase
calculation = input("Enter your choice (1 or 2): ").lower()


#if the user selects "1" or "investment", investment details such aas principle, rate, time and
# interest type(simple or compound) will be asked
if calculation == "1" or calculation == "investment":
    # Investment calculator
    print("\nInvestment Calculator")
    principle = float(input("Enter the amount you are depositing: "))
    rate = float(input("Enter the interest rate (as percentage): ")) / 100
    time = float(input("Enter the number of years you plan on investing: "))
    interest = input("Enter the type of interest you want (simple or compound): ").lower()

    #here I calculate the final amount using the following formulas
    if interest == "simple":
        A = principle * (1 + rate * time)
    elif interest == "compound":
        A = principle * math.pow((1 + rate), time)
    else:
        print("Invalid input for interest type.")
        exit()

        #here will be displayed the result
    print(f"\nAfter {time} years, your investment will be worth: R {A:.2f}")


#if the user selects "2" or "bond", bond details such as present value of the house,
#interest rate, and the number of months for repayment will be asked and I will also calculate below, the monthly
#repayment using the formulas
elif calculation == "2" or calculation == "bond":
    #bond calculator
    print("\nBond Calculator")
    P = float(input("Enter the present value of the house: "))
    i = (float(input("Enter the interest rate: ")) / 100) / 12
    n = float(input("Enter the number of months you plan to take to repay the bond: "))
    repayment = (i * P) / (1 - (1 + i)**(-n))
    print(f"\nYou will have to repay R {repayment:.2f} per month over {n} months.")

#this message will be displayed for invalid options and the program will exit
else:
    print("Invalid input for calculation type.")
    exit()