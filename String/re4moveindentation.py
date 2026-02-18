user_input = input("Enter your input: ")
final_string = user_input.isidentifier()

if final_string == True:
    print("The given string is an identifier")
else:
    print("The given string is not an identifier")
