
print("\n\nAnswer These Questions on a scale from 1 - 10 : \n\n")
#Get loan size
loan_size = int(input("What is your loan size? : "))
while loan_size > 10 or loan_size < 1:
    loan_size = int(input("Please enter a valid rating on the scale"))
#Get credit history
credit_history = int(input("What is your credit history? : "))
while credit_history > 10 or credit_history < 1:
    credit_history = int(input("Please enter a valid rating on the scale"))

#Get income
income = int(input("What is your income"))
while income > 10 or income < 1:
    income = int(input("Please enter a valid rating on the scale"))

#Get down payment
down_payment