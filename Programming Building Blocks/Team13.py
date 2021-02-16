import math

def compute_area_square(side):
    square_area = side*side
    return(square_area)

def compute_area_rect(length, width):
    rect_area = length*width
    return(rect_area)

def compute_area_circle(radius):
    circle_area = math.pi*radius**2
    return(circle_area)

#Get which comp
print("1. Area of Square")
print("2. Area of Rectangle")
print("3. Area of Circle")
print("4. Quit")
user_in = int(input("Which area would you like to compute? : "))
while (user_in != 4) and (user_in == 1 or user_in == 2 or user_in == 3):

    if(user_in == 1):
        #ask for square side lenght
        side_length = float(input("What is the side length of the square? : "))
        #call method with passed args
        square_area = compute_area_square(side_length)

        print(f"The area of the square is : {square_area}")
    elif(user_in == 2):
        #ask for lenght
        #ask for width
        #call method and pass args
        rect_length = float(input("What is the lenght of the rectangle? : "))
        rect_width = float(input("What is the width of the rectangle? : "))

        rect_area = compute_area_rect(rect_length, rect_width)

        print(f"The area of the rectangle is : {rect_area:.2f}")
    elif(user_in == 3):
        #ask for radius
        #call method and pass args
        circ_rad = float(input("What is the radius of the circle? : "))

        circ_area = compute_area_circle(circ_rad)

        print(f"The area of the circle is : {circ_area:.2f}")

        
    else:
        print("Please enter a valid option")
        print("1. Area of Square")
        print("2. Area of Rectangle")
        print("3. Area of Circle")
        print("4. Quit")
        user_in = int(input("Which area would you like to compute?"))


    print("1. Area of Square")
    print("2. Area of Rectangle")
    print("3. Area of Circle")
    print("4. Quit")
    user_in = int(input("Which area would you like to compute?"))
#Check data
#Method computes square area




#call correct method