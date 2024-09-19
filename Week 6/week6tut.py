#Part a
L = [34, 2, 45, 10, -2, 6]
L.sort()
print(L)

#Part b
L = [34, 2, 45, 10, -2, 6]
L.append(13)
print(L)

#Part c
L = [34, 2, 45, 10, -2, 6]
L.reverse()
print(L)

#Part d
L = [34, 2, 45, 10, -2, 6]
print(L.index(34))

#Part e
L = [34, 2, 45, 10, -2, 6]
L.remove(10)
print(L)

#Part f
L = [34, 2, 45, 10, -2, 6]
print(L[1:3])

#Part g
print(L[2:])

#3. Use the range function to create lists
listA = list(range(3, 7))
listB = list(range(18, 10, -2))
listC = list(range(50, 25, -5)) + list(range(5, 35, 5))
print(listA)
print(listB)
print(listC)

# 4. Assume you are given two lists myList1 and myList2, both of unknown sizes (for testing purposes,
# you can create your own). Saving your answers in a script my lists.py, do the following:
# (a) Using only methods from lists, remove the last element from myList1, remove the first element
# from myList2, concatenante these two new lists while adding a string element ’Hello’ in between.
# (b) Same question, without using any list method.

myList1 = [0, 1, 2, 3]
myList2 = [4, 5, 6, 7]

myList1.pop()
myList2.remove(myList2[0])
myList3 = myList1 + myList2
myList3.insert(len(myList1), "Hello")
print(myList3)