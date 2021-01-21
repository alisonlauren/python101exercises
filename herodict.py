
user_input = (input("please enter a word: "))
def word_count(str):
    counts = dict()
    words = str.split()
    
    for letter in words:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    sortedValues = sorted(counts, key=counts.get, reverse=True)
    sortedCounts = {}
    
    for value in sortedValues:
        sortedCounts[value] = counts[value]
    
    return sortedCounts
       
print(word_count(user_input))