number=int(input("Enter the number"))
prime=False
if number ==1 :
    print("The number is a prime number")
for i in range(2,number):
    if number % i ==0:
        prime= True
        break 

if prime :
    print (f"The number {number} is not a prime number")
else:
    print(f"The number {number} is a prime number")
