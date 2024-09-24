L = [34, 2, 45, 10, -2, 6]
print(L)

# Task a: Sort the list
L.sort()
print(L)

# Task b: add element 13 at the end
L = [34, 2, 45, 10, -2, 6]
L.append(13)
print(L)

# Task c: Reverse the order
L = [34, 2, 45, 10, -2, 6]
L.reverse()
print(L)

# Part d: display the index of the element 34
L = [34, 2, 45, 10, -2, 6]
display = L.index(34)
print(display)

# Part e: Remove the element 10
L = [34, 2, 45, 10, -2, 6]
L.remove(10)
print(L)

# Part f:  display the sub-list from the 2nd to the 3rd element included
L = [34, 2, 45, 10, -2, 6]
subList1 = L[1:3]
print(subList1)

# Part g: display the sub-list from the 3rd to the last element included
subList = L[2:len(L)]
print(subList)

# Bonus question: 
Sa = "abcdefghij"
Sb = Sa[:4]*2 + Sa[6:]*2 + Sa[5]
print(Sb) # Expected output: "abcdabcdghijghijf"

# 3. Using the range function, create the following lists:
# (a) [ 3, 4, 5, 6 ]
# (b) [ 18, 16, 14, 12 ]
# (c) [ 50, 45, 40, 35, 30, 5, 10, 15, 20, 25, 30 ]

# Answer a:
list1 = [i for i in range(3, 7)]
list2 = [i for i in range(18, 10, -2)]
list3 = [i for i in range(50, 25, -5)] + [i for i in range(5, 35, 5)]
print(list1)
print(list2)
print(list3)

