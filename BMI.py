user_height=float(input("Enter your height in meters: "))
user_weight=float(input("Enter your weight in kilograms: "))
bmi = user_weight / (user_height ** 2)
print("Your BMI is: ", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <=bmi <24.9:
    print("you are normal weight")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")