user_input=input("Enter the string :")
if len(user_input) <2:
    print("The string is too short , please enter a string with length greater than or equal to 2")
else:
    last_two_chars=user_input[-2:]
    result=last_two_chars * 4
    print(result)