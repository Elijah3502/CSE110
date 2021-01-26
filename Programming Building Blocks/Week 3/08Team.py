
num_of_col_row = int(input("How many columns and rows would you like? : "))
col = 1
row = 1
while(col <= num_of_col_row):
    print()
    while(row <= num_of_col_row):
        print(f"{(row) * col:3}", end=" ")
        row += 1
    col += 1
    row = 1
