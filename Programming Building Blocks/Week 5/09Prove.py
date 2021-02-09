#Show menu
#
item_list = []
cost_list = []
user_in = 1

print("\n\nWelcome to the shopping cart program\n")

while user_in >= 1 and user_in <= 4 : 
    print("\n\n\n")
    print("Please select one of the following : ")
    print("1. Add item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")
    user_in = int(input("Enter an action : "))
    print("\n\n")
    
    if user_in == 1:
        #Get item
        item_add = input("What item would you like to be added to the cart? : ")
        #Add item
        item_list.append(item_add)
        #Get price
        cost_add = float(input("What is the cost of the item? : "))
        #Add Price
        cost_list.append(cost_add)
    elif user_in == 2:
        #View cart
        for i in range(len(item_list)):
            print(f"{i + 1}. {item_list[i]} - {cost_list[i]:.2f}")
    elif user_in == 3:
        #Remove Item
        remove_num = int(input("What item would you like to remove?"))
        
        while remove_num < 0 or remove_num > len(item_list) :
            print("\nThat is not a valid option.  Please choose a good option")
            remove_num = int(input("What item would you like to remove?"))
        
        for i in range(len(item_list)):
            print(f"{i + 1}. {item_list[i]} - {cost_list[i]:.2f}")
        item_list.pop(remove_num - 1)
    elif user_in == 4:
        #Get total
        total = 0.00
        for item in cost_list:
            total += item
        print(f"Total : {total:.2f}")
            
    else:
        print('Ok thanks.')