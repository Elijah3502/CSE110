#Ask positive number
user_num = int(input("Enter a number that is not negative : "))
while user_num < 0 :
    user_num = int(input("Try again!\nEnter a number that is not negative : "))


ask_candy = input("Can I have some candy? : ").upper()
while ask_candy != "YES":
    ask_candy = input("Can I have some candy? : ").upper()
print("Thanks!!")