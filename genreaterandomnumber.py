## generates a random number between 1 and the range given by the user 
import random 
user_input=int(input("Enter the range to generate number"))
result=random.randint(1,user_input)
print("The numbers are",result )