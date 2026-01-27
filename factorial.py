import math

number=int(input("Enter the number to find the factorial"))
if number <0:
    print("Please enter a valid number")
elif number == 0 or number == 1:
    print("The factorial is 1")
else:
    result=math.factorial(number)
    print(f"The factorial of the number{number} is ",result)