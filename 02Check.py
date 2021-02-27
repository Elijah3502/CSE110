#import date/time
import datetime

total = 0.0
#Get subtotal
user_sub = float(input("What is your subtotal? : "))
#check total and date
date = datetime.datetime.now().isoweekday()
#if subtotal > 50$ and is tuesday or wednesday
if(user_sub >= 50 and (date == 3 or date == 4)):
    #subtract 10%
    discount = user_sub - (user_sub*0.10)
    tax = (user_sub*0.06) + discount
    total = discount + tax
else:
    tax = (user_sub*0.06)
    total = user_sub + tax
    
print(f"Total : {total:.2f}")

#add sales tax
    #6%
