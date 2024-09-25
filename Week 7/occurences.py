def occurences(my_str, my_char):
    count = 0
    characterIndices = []
    for i in range(0, len(my_str)):
        if my_str[i].lower() == my_char:
            count += 1
            characterIndices.append(i)
    return count, characterIndices

my_str = "This is a test string"
print(occurences(my_str, "t"))
