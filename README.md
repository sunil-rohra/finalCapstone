# finalCapstone
My Capstone Project.

1.  This is basically a program which gives the option to the user to choose if he wants to do an 
    - investment calculation where he gets interest on his investment 
    - or bond caluctaion where he has to pay interest on the loan.

2.  The input of Investment or Bond does not get affected if the user uses upper or lower case to input.  The program code takes care of it.

3.  **Investment**: We ask the user for the following input.
4.  
    - Amount of money being deposited,
    - The interest rate as a % in numer only, eg 6
    - The number of years being invested,
    - Simple or Compound interest.  This input is to be stored as a variable "interest".
    - Following formula is to be used for interest calculation of simple or compound.
    - Interest Formula:
      - Simple Interest: 𝐴 = 𝑃(1 + 𝑟 × 𝑡) - The Python equivalent is very similar: A = P*(1 + r*t).
      - Compound Interest: 𝐴 = 𝑃(1 + 𝑟)𝑡 - The Python equivalent is slightly different: A = P * math.pow((1+r),t). 
    - In the formula above:
      - ‘r’ is the interest entered above divided by 100, e.g. if 7% is entered, then r is 0.07.
      - ‘P’ is the amount that the user deposits.
      - ‘t’ is the number of years that the money is being invested. 
      - ‘A’ is the total amount once the interest has been applied.
    
4.  We then print out the resultant amount.  You can try and see the difference between simple and compound for a given set of parameters.
    
5.  **Bond**: We ask the user for the following input.
    - The amount of the loan he needs,
    - The interest rate as a number,
    - The number of months in which he will repay the loan.
    - Bond repayment formula: Monthly repayment: = (𝑖 × 𝑃) / 1− (1+𝑖)−𝑛 
    - The Python equivalent is slightly different: Monthly repayment = (i * P)/(1 - (1 + i)**(-n))
    - In the formula above:
      - ‘P’ is the loan amount.
      - ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. 
        Remember to divide the interest entered by the user by 100 e.g. (8 / 100) before dividing by 12.
      - ‘n’ is the number of months over which the bond will be repaid.
 
 6. Calculate the monthly amount to be repaid and print the output as the answer.

