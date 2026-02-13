input_str1=input("Enter the first value ")
input_str2=input("Enter the second value ")
first_string_chars=input_str1[0:2]
second_string_chars=input_str2[0:2]
modified_first_string=second_string_chars + input_str1[2:]
modified_second_string = first_string_chars + input_str2[2:]
print("The modified first string is ", modified_first_string)
print("The modified second string is ", modified_second_string)