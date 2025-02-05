**In the name of Allah**

# 021: Lists
1. Square brackets.
2. Ordered.
3. Mutable.
4. List items aren't unique.
5. Can have different types.
```Python
myList = ["one", 1, True, 100.5]

# Slicing
print(myList[1:4]) # [1, True, 100.5]
print(myList[::2]) # ['one', True]

# Mutability (Editing not replacing)
myList[1:3] = "one", False
print(myList) # ['one', 'one', False, 100.5]
```
> ***Mutability is editing & not replacing.***