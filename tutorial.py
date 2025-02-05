# In the name of Allah

myList = ["one", 1, True, 100.5]

# Slicing
print(myList[1:4]) # [1, True, 100.5]
print(myList[::2]) # ['one', True]

# Mutability (Editing not replacing)
myList[1:3] = "one", False
print(myList) # ['one', 'one', False, 100.5]