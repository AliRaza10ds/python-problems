lower_range=1
upper_range=10

for i in range (lower_range,upper_range):
    for j in range(2,i):
        if i %j ==0:
            break 
        else:
            print(i)
