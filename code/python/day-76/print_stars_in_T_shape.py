rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
mid_col = int(cols/2)
for row in range(0,rows):
    for col in range(0,cols):
        if (row == 0) or (row > 0 and col == mid_col):
            print("*",end="")
        else:
            print(end=" ")
    print()
