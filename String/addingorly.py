user_input=input("Enter your value...:")
if len(user_input) >=3:
    input_last_three_chars=user_input[-3:]
    if input_last_three_chars =="ing":
        print(user_input + "ly")
    else:
        print(user_input + "ing")
else:
    print(user_input)