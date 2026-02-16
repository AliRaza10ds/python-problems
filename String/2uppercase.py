user_input = input("Enter a string : ")

first_four_chars = user_input[:4]

count = 0

for ch in first_four_chars:
    if ch.isupper():
        count += 1

if count >= 2:
    upper_case = user_input.upper()
    print("The string is in uppercase as :", upper_case)
else:
    print("The string can not be converted into uppercase as the first four characters of the given string does not contain at least two uppercase characters")
