#ID badge program

#Get id card data

#Get First Name
first = input("What is your first name? : ")
#Get Last Name
last = input("What is your last name?: ")
#Get Email
email = input("Enter your email: ")
#get Phone Number
phone_number = input("Enter phone number : ")
#Get Job Title
title = input("Enter job title : ")
#Get id number
id_number = input("Enter ID number : ")
#Get hair color
hair_color = input("Enter hair color : ")
#Get Eye Color
eye_color = input("Enter Eye color : ")
#Get Month Started
month_started = input("Enter month started : ")
#Get completed training bool
advanced_completed = input("Has user completed advanced training? (yes/no) : ")
print("\n\n")


#Display ID Card
print("The ID Card is : ")
print("----------------------------------------")
print(last.upper() + ", " + first)
print(title.capitalize())
print("ID : " + id_number)
print("\n" + email.lower())
print(phone_number)
print("\n")
#prints formatted with spacing
print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month_started:14} Training: {advanced_completed}")
print("----------------------------------------")