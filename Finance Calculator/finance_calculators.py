#import math 
import math
#Print introductory text for the calculator in seperate  lines
print("Welcome to Finance Calculator. Please choose wether 'investment' or 'bond' from the menu below to proceed: ")
print("Investment	- to calculate the amount of interest you'll earn on interest")
print("Bond	- to  calculate the amount you'll have to pay on a home loan")
#Crearte input for selction of bond or  investment and change it to lower case for workability
option_input_calculation = input("Please enter option here:  ")
option_input_calculation = option_input_calculation.lower()

#investment track entry 
if option_input_calculation == "investment":
	deposit_amount =  input("Please enter amount you wish to deposit: ")
	interest_rate = input("Please enter the interest rate (%): ")
#the interest entered above divided by 100
	interest_rate = int(interest_rate)/100
	investment_time =   input("Please enter the number of years you wish to invest for: ")
	interest = input("Would you like  'simple' or 'compound' interest: ")
	interest = interest.lower()
#If entry is simple use formula (A =P*(1+r*t)) and print
	if interest == "simple":
		simple_inv_total = float(deposit_amount) * ((1 + interest_rate) * float(investment_time))
		print("This is the total you will recieve on your investment: ")
		print(simple_inv_total)
#If entry is compound use formula (A = P* math.pow((1+r),t)) and print 
	elif interest == "compound":
		coumpound_inv_total = float(deposit_amount) * math.pow((1 + interest_rate), float(investment_time))
		print("This is the total you will recieve on your investment: ")
		print(coumpound_inv_total)
	else:  
		print("Entry is invalid!")

#bond track entry  
elif option_input_calculation == "bond":
	home_value = input("Please input the value of your home here: ")
	home_value = float(home_value)
#the interest entered above divided by 12
	interest_rate_bond = input("Please enter the interest rate (%): ")
	interest_rate = float(interest_rate_bond) / 100 / 12
	repay_time = input("Please enter the number of months you will take to repay this bond (in months): ")
	repay_time = float(repay_time)
#Bond repayment formula x = M = L(I(1 + I)**N) / ((1 + I)**N - 1)
#M = Monthly Payment, L = Loan, I = Interest, N = Number of payments, ** = exponent
	monthly_repayment = home_value * (interest_rate * (1 + interest_rate)
                                ** repay_time) / ((1 + interest_rate) ** repay_time - 1)
	print("This is the amount you will have to payback each month: ")
	print(monthly_repayment)
#Error Message
else:
	print("Entry is invalid!")
