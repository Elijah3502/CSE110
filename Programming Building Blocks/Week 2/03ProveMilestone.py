"""
Need to find : 

Price of a childs meal : Float : 
Price of an adult meal : Float : 
number of children : int : 
number of adults : int : 
sales tax : float :
"""
child_sub = 0.0
adult_sub = 0.0
sub_total = 0.0
total = 0.0
sales_tax = 0.0
tip_total = 0.0
total = 0.0
change = 0.0
#GET CHILD MEAL COST
print("++++++++++++++++++++++++++++++++++++++++++++++")
child_cost = float(input("What is the cost of a child's meal? : $ "))
#GET ADULT MEAL COST
adult_cost = float(input("What is the cost of an Adult's meal? : $ "))
print("++++++++++++++++++++++++++++++++++++++++++++++\n\n")
print("++++++++++++++++++++++++++++++++++++++++++++++")
#GET NUMBER OF CHILDREN
child_num = int(input("How many children are there? : "))
#GET NUMBER OF ADULTS
adult_num = int(input("How many adults are there? : "))
#GET SALES TAX
tax_rate = float(input("What is the sales tax rate? : %"))
print("++++++++++++++++++++++++++++++++++++++++++++++\n\n")
#COMPUTE SUBTOTAL(BEFORE TAXES)
child_sub = child_cost * child_num
adult_sub = adult_cost * adult_num
sub_total = child_sub + adult_sub
#DISPLAY SUB TOTAL
print("\n\nSubtotal : $ " + str(sub_total))
#COMPUTE SALES TAX
sales_tax = sub_total * (tax_rate/100)
#DISPLAY SALES TAX
print("\nSales Tax : " + str(sales_tax))
#ASK FOR TIP
check_tip = input("\n Would you like to add a tip? (yes/no): ")
if check_tip == 'yes' :
    tip_amount = float(input("\nThank you!! \nHow much would you like to tip? : % "))
    tip_total = sub_total * (tip_amount/100)
    #COMPUTE TOTAL
    total = sub_total + sales_tax + tip_total

else :
    #COMPUTE TOTAL
    total = sub_total + sales_tax



#DISPLAY TOTAL
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("Total : $" + str(total))
#GET PAYMENT AMMOUNT
pay_amount = float(input("What is the payment amount? : $"))
#DISPLAY CHANGE
while(pay_amount < total) :
    pay_amount = float(input("Please enter a payment amount more than or equal to the total: $"))
    break
change = pay_amount - total
print(f"Your change is : ${change:.2f}")
print("++++++++++++++++++++++++++++++++++++++++++++++")

#DISPLAY THANK YOU MESSAGE