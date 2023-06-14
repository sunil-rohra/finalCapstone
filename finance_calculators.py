# 1. I was struggling on this one to get the code/program to use the user options 
# 2. How do you select which option to use when user decides either investment or bond
# 3. Also how do select which option to output simple or compound when users makes the selection
# 4. I therefore did a lot of google search and use the idea and function from there.
# 5. I did quite a lot of the code also on my own particularly the outputs

import math



print()

print("Investment   - to calculate the amount of interest you will earn on your investment")
print("Bond         - to calculate the amount you will have to pay on a home loan")
print() # extra print function to get a new line and be neat

user_choice = str(input("Please enter either 'Investment' or 'Bond' from the menu above to proceed: ")).casefold()
# Asking User to make a choice.
# casefold function ensures that code recgnises any form of input by user ie in capitals or lower case.

if user_choice == "Investment".casefold():
# telling program if user has input option investment then to proceed with this course of action.
# program is making the decision.
# This should be explained in course lectures and materials.
    
        P = float(input("How much money are you depositing: "))
        r = float(input("What is the % interest rate you would like to obtain: "))
        r = float(r/100)
        t = float(input("How many years would you like to invest: "))
        user_interest = str(input("Would you like 'Simple' or 'Compound' interest: ")).casefold()
# putting float before input ensures that we can take numbers and decimals as input.
# casefold function helps to recgonise input either as capital or lower case.
# These subtle points to be explained in course materials when they mentioned about lower and upper cases.
    
        if user_interest == "simple".casefold():
            user_interest = P*(1 + r*t)
            A = round(user_interest,2)
            print(f"Your total amount with simple interest after {t} years will be {A:,.2f}.\n")
# using the format funtion "f" to make it neat and short.
# telling the program to choose the option "Simple" when input is simple.
# using the round function to get upto 2 decimals rounded off; otherwise will get too many decimals.
    
        elif user_interest == "compound".casefold():
            user_interest = P * math.pow((1+r),t)
            A = round(user_interest,2)
            print(f"Your total amount with compound interest after {t} years will be {A:,.2f}.\n")

        else:
            print("Please enter either 'Simple' or 'Compound'. Start again.")
  

elif user_choice == "Bond".casefold():
    P = float(input("What is the present value of the house: "))
    i = float(input("What is the rate of interest you would like to pay: "))
    i = float(i/100)/12
    n = float(input("In how many months will you repay the loan: "))
    monthly_repayment = (i * P)/(1 - (1 + i)**(-n))
    M = round(monthly_repayment, 2)
    print(f"You will pay {M:,.2f} per month for {n} months to repay your loan.")

else:
    print("Please choose Investment or Bond. Start again.")


