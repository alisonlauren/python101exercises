num_guess = ' '
print("I'm thinking of a number between 1 and 50, what is it?: ")


while num_guess != "no":
    try:
        num_guess = input("Would you like to try again??: ")
        num_guess = int(num_guess)
        if  num_guess != 33:
            input("Try again?")
        if num_guess == 33:
            print("You got it!")
            break
    except ValueError:
        print(f'Error: You used {num_guess}, Use digits instead.')
