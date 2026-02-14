user_input = input("Enter the value: ")
splitted_input = user_input.split()

result = splitted_input[::2]   

print("The output after removing the odd index is as:", result)
