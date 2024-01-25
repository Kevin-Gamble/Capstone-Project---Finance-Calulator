"""
==========           Title = finance-calculator                      ==========  

Version    = 3.0      
Variable 

Comments   
Bond repayment calculator was incorrect in Version 1.0
interest rate was used as a whole number e.g. 7 for 7% 
it should be 7/100 = 0.07 (annual interest)
then annual (interest) / 12 = (monthly interest)


Author     = Kevin Gamble
Student ID = KG23090010040

Note to reviewer - Once fully versed with Git, version control and 
                   comments will be utilised and header block pseudo code shall be stored in a text file as advised during a Lecture.

==================================================================
-----psuedo code-----
import the math module to perform mathematical functions

output to the screen the choices of either investment or bond investments.
ask the user to choose from investment or bond investments

if the user enters "investment", "Investment" or "INVESTMENT" then ask for the following
    The amount of money they are depositing
    The interest rate as a percentage e.g. 8 not 8%
    The number of years they plan on investing
    The interest type e.g. "simple" or "compound" interest

    if the answer is "simple" then
        calculate the simple interest e.g. -
        simple_interest = money_depositing * (1 + interest_rate_percent / 100 * years_investing)

    else if the is "compound" then
        calculate the compound interest e.g. -
        compound_interest = money_depositing * (1 + interest_rate_percent / 100 * years_investing)^2 
    else output an error message "You must enter simple or compound" then end

    output the amount they will receive after the given period at the specified interest

else if the user enters Bond, bond or BOND ask for the following
    The present value of the house e.g. 100000
    The interest rate as a percentage e.g. 7 not 7%
    The number of months they plan to replay the bond e.g. 120
    calculate the bond_repayment e.g.
    bond_repayment =  (((interest_rate / 100)/ 12) * house_value) /
                      (1 - (1 + (interest_rate / 12))**(-num_of_months))
    output 

else output to the screen "You must enter either "investment" or "bond"
end
==================================================================
"""
#Import the math module to perform mathematical functions
import math

#Crude method to delete previous line in the terminal i.e the path and filename
print('\033c')

#Present Title and options
print()
print("~~~~~~~~~~~~~~~~~~~~~~~ Investment and Bond calculator ~~~~~~~~~~~~~~~~~~~~~~~ ")
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()

#Get user input and check its valid to continue
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#If the user has Entered investment
if user_choice.lower() == "investment":
    #Get user inputs for the calculation and the interest type
    money_depositing = input("Enter the amount of money you are depositing e.g. 10000 : ")
    interest_rate_percent = input("Enter the interest rate as a percentage e.g. 8 not 8%   : ")
    no_of_years_investing =  input("Enter the number of years you plan on investing         : ")
    interest_type = input("Do you want 'simple' or 'compound' interest             : ")

    #While there is a valid input perform the correct calculation otherwise output an error and end
    while True:
        #If simple interest is entered calculate the simple interest
        if interest_type == ("simple"):
            receive_amount = int(int(money_depositing) * (1 + int(interest_rate_percent)
                            / 100 * int(no_of_years_investing)))

        #If compound interest is entered calculate the compound interest 
        elif interest_type == ("compound"):
            receive_amount = int(int(money_depositing) * math.pow
                            (1 + ((int(interest_rate_percent) / 100)), int(no_of_years_investing)))

        #Otherwise output an error message and end
        else:
            print()
            print("Incorrect choice ! Please enter 'simple' or 'compound'")
            break

        #All ok therefore output calculated and associated values to the screen
        print()
        print(f"You will receive £{receive_amount} after {no_of_years_investing}" \
                f" years at an interest rate of {interest_rate_percent}%")
        break
#Else if the user has selected Bond
elif user_choice.lower() == "bond":
    house_value = input("Enter the present value of the house. e.g. 100000     : ")
    interest_rate_percent = input("Enter the interest rate as a percentage e.g. 8 not 8% : ")
    months_to_repay = input("Enter the number of months you plan to repay the bond : ")

    #V2.0 repayment now calculated correctly!
    repayment = int(((int(interest_rate_percent) / 100) / 12 
                    * int(house_value)) 
                    / (1 - (1 + (int(interest_rate_percent) / 100) / 12) 
                    ** int(- int(months_to_repay))))
    print()
    print(f"The monthly repayment will be £{repayment}")

#The user has not entered a valid input i.e. 'investment' or 'bond'- output error message
else:
    print()
    print("Incorrect choice ! Please enter 'investment' or 'bond'.")
