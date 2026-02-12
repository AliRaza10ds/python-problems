user_input=input("Enter your input string: ")
user_choiice=input("Enter the character whose frequency you want to find :")
if user_choiice in user_input:
    frequency=user_input.count(user_choiice)
    print("The frequency of the character ",user_choiice,"is",frequency)
else:
    print("The entered character is not present in the given input, please enter a valid character")