import math

#Team activity for unit 3

"""
Write a program to compute the areas of three different shapes. Prompt for the necessary information, 
then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
"""
#Area of a Square
#Get Side length of square in cm
square_length = float(input("What is the side lenght of the square? : "))
#Calculate area in cm^2
square_area = square_length **2
#Display area of square
print("The area of the square is : " + str(square_area) + "cm^2 / " + str(square_area * 10000) + "m^2" )
#Area of a Rectangle

#Get Length in cm
rect_length = float(input("What is that length of the rectange? : "))
#Get width in cm
rect_width = float(input("What is the width of the rectangle? : "))
#Calculate area
rect_area = rect_length*rect_width
#Display area in cm^2
print("The area of the rectangle is : " + str(rect_area) + "cm^2 / " + str(rect_area * 10000) + "m^2\n")


#Area of a circle
#Get radius in cm
circle_rad = float(input("What is the radius of the circle? : "))
#Stretch number 1 : Use python pi function
#Calculate area
# - Imported the math module and uses the .pi method
circle_area = math.pi*(circle_rad**2)
#Display area in cm^2
print("The area of the circle is : " + str(circle_area) + "cm^2  / " + str(circle_area * 10000) + "m^2/n")

#Stretch 2 : 
#Ask for single value
init_value = float(input("Enter an inital value to get areas and volumes : "))
#Calculate area
#Area of a square
square_area_stretch = init_value**2
#Area of circle
circle_area_stretch = math.pi*(init_value**2)
#Calculate Volume
#Cube Volume
cube_volume = init_value**3
#Sphere Volume
sphere_volume = (4/3) * math.pi * (init_value**3)
#Display areas

print("The area of the square is : " + str(square_area_stretch))
print("The area of the circle is : " + str(circle_area_stretch))
#Display volume
print("The volume of the cube is  : " + str(cube_volume))
print("The volume of the sphere : " + str(sphere_volume))