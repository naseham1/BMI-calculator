# Request the user to enter their weight in kg and height in m
weight = float(input("Enter your weight in kg"))
height = float(input("Enter your height in m"))

# Calculate and print the users BMI using the user input
BMI = (weight/(height*height))
print(BMI)

# Create if statements to print the users weight categeory based on their BMI
if BMI >= 30:
    print("You are obese")
if BMI >= 25:
    print("You are overweight")
if (BMI >= 18.5) and (BMI <25):
    print("You are a normal weight")
if BMI < 18.5:
    print("You are underweight")
