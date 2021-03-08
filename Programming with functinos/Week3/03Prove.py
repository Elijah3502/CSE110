#imports csv functions
import csv
import datetime
from os import read

#Dictionary for storing products
prod_dict = {

}
#Dictionary for storing requests
req_dict = {

}

#Dictionary for the receipt
receipt_dict = {

}

number_of_items = 0

subtotal = 0

current_date_and_time = datetime.datetime.now()

# Format the current date and time to include only
# the day of the week, the hour, and the minute.
formatted_dt = current_date_and_time.strftime("%A %I:%M %p")

#Open products.csv
with open("/Users/elijah/BYUI/Programming with functinos/Week3/products.csv") as products:
    reader = csv.reader(products)
    
    #Skip first row
    next(reader)

    #Populate Dictionary
    for row in reader:
        #Elements
        #0 - Product Number
        prod_num = row[0]
        #1 - Product Name
        prod_name = row[1]
        #2 - Retail Price
        prod_cost = row[2]

        #add element to dict
        prod_dict[prod_num] = [prod_name,prod_cost]
    
    

#Open requests.csv
with open("/Users/elijah/BYUI/Programming with functinos/Week3/request.csv") as request:
    reader = csv.reader(request)

    next(reader)

    for item in reader:
        # 0 - Product Number
        prod_num = item[0]
        # 1 - Quantity
        prod_quant = item[1]

        #add item to dictionary
        req_dict[prod_num] = prod_quant

# Display Products
#print(f"THIS IS THE PRODUCTS DICT : \n{prod_dict}")
# Display Requests
#print(f"THIS IS THE REQUEST DICT : \n{req_dict}")


print("\nRequested Items : \n")
for req_item in req_dict:
    #receipt_dict[req_item] = [prod_dict[req_item]]
    name = prod_dict[req_item][0]
    cost = prod_dict[req_item][1]
    count = req_dict[req_item][0]

    subtotal += (float(cost) * int(count))

    

    print(f"{name:.15} : {count:.2} @ ${cost:.5} \n")

tax = subtotal * 0.06
total = subtotal + tax

print("------------------------------\n")
print(f"Subtotal : {subtotal:.2f}")
print(f"Tax : {tax:.2f}")
print(f"Total : {total:.2f}")
print("\n------------------------------\n")
print(f"Date and time of checkout : {formatted_dt}\n\n")


    