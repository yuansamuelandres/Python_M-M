# In the name of Allah

''' #024 & #025: Tuples & Methods '''
# Tuple items are enclosed in parentheses & can be removed.
# Tuple items are ordered & indexed.
# Tuples are immutable.
# Tuple items aren't unique.
# Tuples can have different data types.
# Strings & lists operators are used in tuples.

# Tuple with one element ("",) :
mine = "Yuan",
print(type(mine))   # 'tuple'


# Tuple Concatenation
a = 1, 2, "C", 3
b = 4, 5
c = a + b
print(c)    # (1, 2, 3, 4, 5)

# Indexing
print("The position of index is: {:d}".format(c.index(3)))  # The position of index is: 2
print(f"The position of index is: {c.index(3)}")    # The position of index is: 2

# Destructing
x, y, _, z = a
print(x)    # 1
print(y)    # 2
print(z)    # 3