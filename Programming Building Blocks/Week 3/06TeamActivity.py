#Get the age of rider_one
#init variables
age_two = 0


age_one = int(input("What is the age of the first rider? : "))
#Get the height of rider_one
height_one = int(input("What is the height of the first rider? : "))
#Ask if second rider
is_second = bool(input("Is there a second rider? (true/false): "))
#Get age of rider_two
if is_second:
    age_two = int(input("What is the age of the second rider? : "))
    #Get the height of rider_one
    height_two = int(input("What is the height of the second rider? : "))
#Check age and height of one                check age of two
elif (age_one < 18 or height_one < 62) or (age_two < 18):
    print("You cannot ride the ride!")
elif (age_one >= 18 and height_one >= 62) or (age_two >= 18):
    print("You can ride the ride!!\n\nEnjoy the ride!!")
else:
        if age_one < 18 or height_one < 62:
            print("You cannot ride the ride!")
        else:
            print("You can ride the ride!!\n\nEnjoy the ride!!")
