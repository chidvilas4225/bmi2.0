#Calculates the BMI of a person and gives output according to it.
weight = float(input("Enter your Weight : "))
height = float(input("Enter your Height : "))

bmi = weight / (height ** 2)
print(f"Your BMI is :{round(bmi)} ")
if bmi < 18.5:
    print("You are under weight")
elif bmi > 18.5 and bmi <25:
    print("You are Normal weight")
elif bmi > 25 and bmi <30:
    print("You are over weight")
elif bmi > 30 and bmi <35:   
    print("You are obese")
else:
    print("You are clinically obese")

Output :

# Enter your Weight : 56
# Enter your Height : 1.54
# Your BMI is :24 
# You are Normal weight.
