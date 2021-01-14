

side = int(input("How big is the square?  : "))

print("Look at your masterpiece!") 

for i in range(side):
    for i in range(side):
        print('❄️', end = ' ')
    print()

    #or 

one = 5
two = 5

counter = 0
thing = '*' * two

while counter < one:
    print(thing)
    counter += 1

