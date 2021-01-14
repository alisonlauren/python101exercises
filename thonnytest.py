def make_formal_greeting(name, title, location):
    return f"{intro} {name}, the {title} of {location}"

intro = "Now comes"
result = make_formal_greeting("Rob", "King", "The North")
print(result)

result = make_formal_greeting("The North", "Rob", "King")
print(result)

result = make_formal_greeting("Sadie", "Doggie", "Kingwood")
print(result)

def convert_string(number_list):
    string_list = []
    for number in number_list:
        string_list.append(str(number))
    return string_list

breakfast_count = [2, 3, 9986]
waffle_count = [5, 5555, 55555, 55555]

print(convert_string(breakfast_count));
print(convert_string(waffle_count));