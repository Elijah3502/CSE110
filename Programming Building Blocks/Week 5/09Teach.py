#Ask for list of numbers
#Zero ends

user_in = -1
num_list = []
num_sum = 0
num_average = 0
num_max = 0


print("Enter a list of numbers, type 0 when finished : ")

while user_in != 0:
    user_in = int(input("Enter a number : "))
    num_list.append(user_in)
    num_sum += user_in
    num_average = num_sum
    #Get largest
    if user_in > num_max :
        num_max = user_in
num_average = num_average/(len(num_list) - 1)

print(f"This is the sum : {num_sum}")
print(f"This is the average : {num_average}")
print(f"This is the largest number : {num_max}")
