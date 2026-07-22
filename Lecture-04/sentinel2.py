
row = int (input("How many rows?: "))
columns = int(input("How many columns? :"))
for i in range(row):
    for j in range(columns):
        print("*", end="")
    print()