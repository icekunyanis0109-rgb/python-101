weight = input("Enter your weight in Kilograms: ")
weight = int(weight)

height = input("Enter your height in meters: ")
height = float(height)

bmi = weight / (height ** 2) 

print("Your BMI is: " + str(format(bmi, ".2f")))

