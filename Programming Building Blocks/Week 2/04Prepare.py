#Convert program

get_temp = float(input("What is the temperature in Farenheit? : "))
convert_temp = ((get_temp - 32) * 5) / 9
print(f"The Temperature in celsius is {convert_temp:.2f} degrees.")