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

print("-"*100)

print("Welcome to finance calculator! We can calculate one of two options: \n")                       # Introduction to program

print("Investment - to calculate the amount of interest you'll earn on your investment. \n ")         # Define what service they require

print("Bond - to calculate the amount you'll have to pay on a home loan. \n")                         # Define what service they require

print("Enter 'e' to exit\n")

print("-"*100)

user_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:")     # User input required


# Investment block
if user_choice.lower() == 'investment':
    deposit_amnt1 = input("Please enter the amount of money you would like to deposit (numerals exclusively): \n")   # Deposited amount vairable 
    deposit_amnt = float(deposit_amnt1)                                                                              # Casting string into integer

    i_interest_rt1 = input("Please enter the given interest rate (numerals exclusively) : \n")                       # Invesment interest rate variable
    i_interest_rt2 = float(i_interest_rt1)                                                                           # Casting string into integer 

    i_interest_rt =  i_interest_rt2 / 100                                                                            # Divide the variable by 100 to find percentage in decimal form 
    year_invest1 = input("Please enter the intended years (numerals exclusively) : \n")                              # Years of investment variable 
    year_invest = float(year_invest1)                                                                                # Casting string into integer

# Simple or Compoud interest block
    
    simp_comp_choice = input("Enter either simple or compound for the type of interest to be calculated: ")          
    if simp_comp_choice.lower() == "simple":
        sim_intr_form = deposit_amnt *(1 + i_interest_rt*year_invest)                                                # Simple interest formula being implemented on input
        is_roundup = round(sim_intr_form, 2)
        print(f"The total amount after {year_invest} years, using simple interest is: £{is_roundup}!")

    elif simp_comp_choice.lower() == "compound":
        comp_intr_form = deposit_amnt * math.pow((1+i_interest_rt),year_invest)                                      # Compound interest formula being implemented on input
        ic_roundup = round(comp_intr_form, 2)
        print(f"The total amount after {year_invest} years, using compound interest is: £{ic_roundup}")
    else:
        print("No choices were entered, goodbye.")

# Bond block

elif user_choice.lower() == "bond":
    home_val1 = input("Please enter the present value of your house (numerals exclusively): \n")                # Current market value of house 
    home_val = (int(home_val1))                                                                                 # Casting string into integer

    b_interest_rts1 = input("Please enter the monthly interest rate on your house (numerals exclusively): \n")  # Percentage needs to be number / 100 - finding percentage
    b_interest_rts2 = float(b_interest_rts1)                                                                    # Casting string into integer
    b_interest_rts = (b_interest_rts2 / 100) / 12                                                               # Divide the variable by 100 = the decimal point version
    
    monthly_rep1 = input("Please enter the total amount of months to repay (numerals exclusively): \n")         # Months in which the bond will be repaid in 
    monthly_rep = int(monthly_rep1)                                                                             # Casting string into integer

    bond_repay_form = (b_interest_rts * home_val)/(1 - (1 + b_interest_rts)**(-monthly_rep))                    # Formula being implemented on input

    b_roundup = round(bond_repay_form, 2)                                                                       # Rounding function used on the total variable

    print(f"Your monthly repayment amount is £{b_roundup}!")                                                   # Final bond print statment for the total 

elif user_choice.lower() == "e" and "exit":                                                                    # If the user enters e or exit they will leave
    print("You have chosen to leave, Goodbye!")

else: print("Unfortunately no given choice was entered, Good bye!")