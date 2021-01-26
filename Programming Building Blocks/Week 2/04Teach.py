"""
Team Activity
Week 04
Purpose: Determine how fast an object will fall using the formula:
v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
"""
import math
print("To calculate how fast an object will fall, enter these informations:")
#input mass (in kg)
m = float(input("Mass (in kg): "))
#input acceleration due to gravity
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
#input time (in seconds)
t = float(input("Time (in seconds): "))
#input density of fluid
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
#input cross sectional area of projectile (in square meters)
A = float(input("Cross sectional area (in m^2): "))
#input drag constan
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
#Compute the value for the inner value c
c = (1 / 2) * p * A * C
#show value of c
print(f"The inner value of c is: {c:.3f}")
#Compute and display the overall velocity
v = math.sqrt(m * g / c) * (1 - math.exp((-1*(math.sqrt(m * g * c) / m ))*t))

print(f"The velocity after 10.0 seconds is : {v:.3f}")




#Stretch 1
"""
.75kg Alexa speaker
g = 9.8
csa = 25.51


To calculate how fast an object will fall, enter these informations:
Mass (in kg): 0.75
Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
Time (in seconds): 10
Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
Cross sectional area (in m^2): 25.51
Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5
The inner value of c is: 8.291
The velocity after 10.0 seconds is : 0.942


Boulder = 68kg
Mass (in kg): 68     
Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
Time (in seconds): 10
Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
Cross sectional area (in m^2): 0.676
Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5
The inner value of c is: 0.220
The velocity after 10.0 seconds is : 45.781
"""

#Stretch 2
"""
Alexa Speaker : 
Earth V = 0.942
Jupiter V = 1.473

Boulder : 

Earth V = 45.781
Jupiter V = 80.865

"""

#Stretch 3

#Terminal Velocity = 

print("\n\nTHE TERMINAL VELOCITY IS : " + str(math.sqrt(m * g / c)))