user_input=input("Enter the string")
given_string_length=len(user_input)
if given_string_length % 4 ==0:
    reverse_string=user_input [::-1]
    print("The reverse of the given string is as :", reverse_string)
else:
    print("the  given string is not a multiple of 4 ", user_input)

