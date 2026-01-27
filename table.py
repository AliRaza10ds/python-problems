number=int(input("Enter the number to get the table"))
if number ==0:
    print("PLease enter the number greater than 0")
else:
    for i in range(1,11):
        table=number * i
        print(table)