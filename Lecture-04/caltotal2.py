max = int(input("Enter number:"))
total = 0.0

print("This program calculate the sum of")
print(max, "numbers you will enter.")

for counter in range(max):
    number = int(input("Enter number:"))
    total = total + number
    
print("The total is", total)