empty_list=[]
user_input=input("Enter your values...")
splitted_user_input=user_input.split()
for words in splitted_user_input:
    empty_list.append(len(words))
    max_length=max(empty_list)

max_len_char=empty_list.index(max_length)
print("The longest word is",max_len_char,"and its length is ",max_length)