rows = int(input("How many rows?: "))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end="")
    print()