import math

# investment - to calculate the amount of interest you'll earn on your investment
# bond       - to calculate the amount you'll have to pay on a home loan

input_investment = 'investment'
input_bond = 'bond'

option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if option == input_investment:
    P = (int(input("Enter your deposit amount:")))
    r = (int(input("Enter your interest rate:")))/100
    t = (int(input("Enter how many years you are planning on investing:")))
    interest = (str(input("Enter either 'simple' or 'compound' depends on your interest: ")))

    if interest == str("simple"):
        A = P*(1+r*t)
        print("You will earn £" + " " + str(A) + " " + "by the end.")
              
    elif interest == str("compound"):
        A = P * math.pow((1+r),t) 
        print ("You will earn £" + " " + str(A) + " " + "by the end.")
        

    else:
        print("Enter a valid answer to get a result.")


elif option == input_bond:
    P = (int(input("Enter the present value of your property:")))
    i = (int(input("Enter the monthly interest rate:"))/100)/12
    n = (int(input("Enter the number of months you are planning to repay the bond:")))
    repayment= (i * P)/(1 - (1 + i) * (-n))   

    print ("You have to pay" + " " + str(repayment) + " " + "per month")



else:
    print("Invalid option. Please enter either 'investment' or 'bond'.")