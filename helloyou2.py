user_name = input("Hey you, what's your name? ")
greeting = f"Hello {user_name}, it\'s so great to meet you!"
count_letters = len(user_name)
letters_of_name = f"Your name has {count_letters} in it!"
print(greeting.upper())
print(letters_of_name)



user_input = int(input("Give me a number: "))
result = user_input * user_input
greeting2 = f"Thanks! Your number multiplied by itself is {result}"
print(greeting2)