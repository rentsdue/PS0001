mystr = ["Thomas", "peyrin_", "Jakob", "Alex", "HOKITKWANKITHOKWAN"]
sorted_strings = sorted(mystr, key = lambda x: x[1:])
sorted_strings_length = sorted(mystr, key = lambda x: len(x))

print(sorted_strings)
print(sorted_strings_length)