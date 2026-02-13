user_input=input("Please enter your input")
first_character=user_input[0]
modified_string=user_input.replace(first_character,'$')
final_string=first_character + modified_string[1:]
print("The string after the replacement of first character with the $ is :", final_string)

