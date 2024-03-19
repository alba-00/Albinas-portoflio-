''' 
Pseudo Code for finance_calculator.py:

Import maths module 

Create variables: 

1.) Users_choice 


2.) Option 1: Investment

Steps of input: 

1. amount of money to be deposited 
input question to user - (float)

2. interest rate (%) - [exclusively numbers] 
input question to user - (float)

3. years for said planned investment 
input question to user - (float)

4. choice between simple/compound interest [.lower()]  
input choice between simple and compound interest to the user

2.b)
Choice between: simple interest or compound interest

1. create formula for simple interest
2. create formula for compound interest

output answer

END

3.) Option 2: Bond 

Steps of input: 

1. present value of their hous e.g. 100000 [exclusively numbers] 
input question to user - (float)

2. interest rate e.g. 7 [exclusively numbers]
input question to user - (float)

3. number of months they plan to take to repay the bond e.g. 120 [exclusively numbers]
input question to user - (float)

3.c) create formula for bond_repayment

4. output answer - calc total money user will have to repay each month 

END

If the user doesnt enter any valid input:
else - print(appropriate error message) 

 '''

import math

def calculate_investment():
    deposit_amnt = float(input("Please enter the amount of money you would like to deposit: "))
    i_interest_rt = float(input("Please enter the given interest rate: ")) / 100
    year_invest = float(input("Please enter the intended years: "))

    simp_comp_choice = input("Enter either 'simple' or 'compound' for the type of interest to be calculated: ")
    if simp_comp_choice.lower() == "simple":
        sim_intr_form = deposit_amnt * (1 + i_interest_rt * year_invest)
        print(f"The total amount after {year_invest} years, using simple interest is: £{round(sim_intr_form, 2)}")
    elif simp_comp_choice.lower() == "compound":
        comp_intr_form = deposit_amnt * math.pow((1 + i_interest_rt), year_invest)
        print(f"The total amount after {year_invest} years, using compound interest is: £{round(comp_intr_form, 2)}")
    else:
        print("Invalid choice for interest type.")

def calculate_bond():
    home_val = float(input("Please enter the present value of your house: "))
    b_interest_rts = (float(input("Please enter the monthly interest rate on your house: ")) / 100) / 12
    monthly_rep = int(input("Please enter the total amount of months to repay: "))

    bond_repay_form = (b_interest_rts * home_val) / (1 - (1 + b_interest_rts) ** (-monthly_rep))
    print(f"Your monthly repayment amount is £{round(bond_repay_form, 2)}")

def main():
    user_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:")
    if user_choice.lower() == 'investment':
        calculate_investment()
    elif user_choice.lower() == 'bond':
        calculate_bond()
    elif user_choice.lower() == 'e' or user_choice.lower() == 'exit':
        print("You have chosen to leave, Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()