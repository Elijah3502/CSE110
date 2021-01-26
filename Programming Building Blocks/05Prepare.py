#Get first number
num_one = int(input("Enter a number : "))
#Get second number
num_two = int(input("Enter a second number : "))
#Compare numbers
#Display correct message
if num_one > num_two:
    print("The first number is greater")
if num_one < num_two:
    print("The second number is greater")
else:
    print("The numbers are equal")

#Get fav animal
user_animal = input("What is your favorite animal? : ")
#Compare animals
if user_animal.upper() == "DOG":
    print("That is my favorite animal too!!")
else : 
    print("That one is not my favorite")
#Display comparison