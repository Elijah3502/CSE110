import math

"""
Program gets the volume of the tire
"""

#Get the tire width
print("\n\n\n--------------------------------------------------------")
tire_width = float(input("Enter the width of the tire in mm (ex 205) : "))
print()
while(tire_width <= 0):
    print("Please enter a number greater than 0")
    tire_width = float(input("Enter the width of the tire in mm (ex 205) : "))
    

#Get the aspect ratio
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60) : "))
print()
while(tire_ratio <= 0):
    print("Please enter a number greater than 0")
    tire_width = float(input("Enter the aspect ratio of the tire (ex 60) : "))
#Get the diameter of the tire
tire_diameter = float(input("Enter the diameter fo the tire in inches (ex 15) : "))

while(tire_diameter <= 0):
    print("Please enter a number greater than 0")
    print()
    tire_width = float(input("Enter the diameter fo the tire in inches (ex 15) : "))
print("--------------------------------------------------------")
#Calculate volume
# Volume = (pi*(width**2)*aspect_ratio*(width*aspect + 2540 * diameter))/10000000
tire_volume = (math.pi * (tire_width**2)*tire_ratio*(tire_width*tire_ratio + 2540 * tire_diameter))/10000000
#Display the volume
print(f"\n\nThe volume of the tire is : {tire_volume:.2f}\n\n")