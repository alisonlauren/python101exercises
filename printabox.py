print("Welcome to Print-A-Box: ")
width = int(input("Width?: "))
height = int(input("Height?: "))

count = 1
while count <= width:
    if count == 1 or count == width:
        print("*" * height)
    else:
        print("*",(" " * (height-8)), "*")
    count = count + 1
    
    