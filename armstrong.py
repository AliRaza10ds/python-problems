number=int(input("Enter the Number"))
length=len(str(number))
temp=number
sum =0
while temp > 0:
    digit= temp % 10
    sum += digit **length
    temp = temp //10

if sum == number:
    print("The number is Armstrong Number")
else:
    print("The number is not an Armstrong Number")
