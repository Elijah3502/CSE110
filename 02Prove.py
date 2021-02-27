import math

"""
Program gets the volume of the tire
"""
width_check = True
ratio_check = True
diameter_check = True


#Method checks data entered by the user
def check_data(min, max, userInput):
    #sets init check value
    is_valid = False

    #while the check has not been done, or has had a problem
    while not is_valid:
        print()
        #check if is Int > 0
        if(not userInput.isdecimal()):
            print(f"\"{userInput}\" is not a valid input. ")
            userInput = input(f"Please enter a number between {min} and {max} : ")
        #check if num is in range
        elif(int(userInput) > max or int(userInput) < min):
            userInput = input(f"Please enter a value within {min} and {max} : ")
        #if no problem sets true
        else:
            is_valid = True
    #returns valid data
    return int(userInput)

#Get the tire width
print("\n\n\n--------------------------------------------------------")
tire_width = input("Enter the width of the tire in mm (ex 205) : ")
print()
#check data
tire_width = check_data(180, 400, tire_width)


#Get the aspect ratio
tire_ratio = input("Enter the aspect ratio of the tire (ex 60) : ")
print()
tire_ratio = check_data(45,70, tire_ratio)


#Get the diameter of the tire
tire_diameter = input("Enter the diameter fo the tire in inches (ex 15) : ")
print()
tire_diameter = check_data(12, 28, tire_diameter)

print("--------------------------------------------------------")


#Calculate volume
tire_volume = (math.pi * (tire_width**2)*tire_ratio*(tire_width*tire_ratio + 2540 * tire_diameter))/10000000

#Display the volume
print(f"\n\nThe volume of the tire is : {tire_volume:.2f}\n\n")
