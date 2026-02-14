user_input=input("Enter your values...")

user_choice=int(input("Enter the number of character you want to remoove from the value that you have entered..."))
if user_choice > len(user_input):
    print("invalid choice,,please enter a valid number")
else:
    del user_input[user_choice -1]
    print("The value after the deletion is as follows",user_input)
