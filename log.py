user_input=float(input("Enter the number to find the logarithm :"))
import math
if user_input <=0:
    print("Please enter a valid number grater than 0 ")
else:
    logarithm=math.log(user_input)
    print("The log value of ",user_input,"is ",logarithm)