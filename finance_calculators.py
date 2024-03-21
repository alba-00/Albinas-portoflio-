''' 
Pseudo Code for finance_calculator.py:

Import maths module 

START
Display options for 'investment', 'bond', or 'exit'.
Accept user choice.
class(investment)
If choice is 'investment':
   Prompt for deposit amount, interest rate, and investment duration.
   Calculate and display either simple or compound interest based on user input.
class(bond)
If choice is 'bond':
   Prompt for house value, monthly interest rate, and repayment duration.
   Calculate and display monthly repayment amount for the bond.
class(menu)
If choice is 'exit':
   Display a goodbye message and end the program.
If choice is invalid:
   Display an error message and prompt again.
END

 '''

import math

# Investment Function
def calculate_investment():
    # Prompt user for deposit amount, interest rate, and investment duration.
    deposit_amnt = float(input("Please enter the amount of money you would like to deposit: "))
    i_interest_rt = float(input("Please enter the given interest rate: ")) / 100
    year_invest = float(input("Please enter the intended years: "))

    # Provide choice between simple or compound interest
    # Calculate and display either simple or compound interest based on user input.
    simp_comp_choice = input("Enter either 'simple' or 'compound' for the type of interest to be calculated: ")
    if simp_comp_choice.lower() == "simple":
        sim_intr_form = deposit_amnt * (1 + i_interest_rt * year_invest)
        print(f"The total amount after {year_invest} years, using simple interest is: £{round(sim_intr_form, 2)}")
    elif simp_comp_choice.lower() == "compound":
        comp_intr_form = deposit_amnt * math.pow((1 + i_interest_rt), year_invest)
        print(f"The total amount after {year_invest} years, using compound interest is: £{round(comp_intr_form, 2)}")
    else:
        print("Invalid choice for interest type.")

# Bond Function 
def calculate_bond():
    # Prompt for house value, monthly interest rate, and repayment duration.
    home_val = float(input("Please enter the present value of your house: "))
    b_interest_rts = (float(input("Please enter the monthly interest rate on your house: ")) / 100) / 12
    monthly_rep = int(input("Please enter the total amount of months to repay: "))

    # Calculate and display monthly repayment amount for the bond.
    bond_repay_form = (b_interest_rts * home_val) / (1 - (1 + b_interest_rts) ** (-monthly_rep))
    print(f"Your monthly repayment amount is £{round(bond_repay_form, 2)}")

# Main Menu Function 
def main():
    print("-"*100)
    print("Welcome to finance calculator! \n")
    print("Investment - to calculate the amount of interest you'll earn on your investment.\nBond - to calculate the amount you'll have to pay on a home loan.\nExit\n")                   
    print("-"*100)
    user_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:")
    if user_choice.lower() == 'investment':
        calculate_investment()
    elif user_choice.lower() == 'bond':
        calculate_bond()
    # Exiting the Menu
    elif user_choice.lower() == 'e' or user_choice.lower() == 'exit':
        print("You have chosen to leave, Goodbye!")
    else:
        print("Invalid choice.")

# Calling Main Menu Function
if __name__ == "__main__":
    main()