# Using only methods from lists, remove the last element from myList1, remove the first element
# from myList2, concatenante these two new lists while adding a string element "Hello" in between.

myList1 = ["Word", "Example String", 44, 55, "Another word"]
myList2 = [1, 2, 3, 4, "Random string"]

myList1.pop()
myList2.pop(0)

concat = myList1 + ["Hello"] + myList2
print(concat)

# Same question, without using any list method.

myList1 = ["Word", "Example String", 44, 55, "Another word"]
myList2 = [1, 2, 3, 4, "Random string"]

del myList1[len(myList1())]
del myList2[0]
concat = myList1 + ["Hello"] + myList2