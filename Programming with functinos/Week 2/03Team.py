import csv

#Open the file
stud_data = {
    
}

def check_data(number):
    is_good = False
    user_data = number
    while not is_good:
        if((not user_data.isdigit()) or (len(str(user_data)) != 9)) :
            user_data = input("Please enter a valid I-Number : (XX-XXX-XXXX) : ")
            user_data.replace("-","")
            print(f"THIS IS THE NOT RIGHT NUMBER : {user_data}")
        else:
            is_good = True
    return user_data

#Opens file
with open("/Users/elijah/BYUI/Programming with functinos/Week 2/pupils.csv") as student_info:
    #Reads file
    reader = csv.reader(student_info)
    #Goes to next time
    next(reader)
    #loops through
    for item in reader:
        #Sets data
        i_number = item[0]
        student_name = item[1]

        #Adds data to dict
        stud_data[i_number] = student_name
 
#Print Dictionary
print(stud_data) 
print("\n\n\n")
#Gets I-number from user
    #user_input = input

    #Gets input
user_in = input("Please enter an I-Number (XX-XXX-XXXX) : ")
#filters input
user_in = user_in.replace("-","")
#prints found data
checked_number = check_data(user_in)

print(stud_data[user_in])



