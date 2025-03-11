# In the name of Allah

''' #023: Lists Methods II '''
# Clearing
a = [1, 2, 5]
a.clear()

# Copying
b = [1, 2, 3, 4]
c = b.copy()    # Shallow Copy


# Counting
d = [1, 2, 1, 33, 2, 5, 1]
print(d.count(1))   # 3

# Indexing
print(d.index(2))   # 1

# Inserting (Before the index)
d.insert(0, "Sam")
print(d)    # ['Sam', 1, 2, 1, 33, 2, 5, 1]

# Popping
print(d.pop(-3)) # 2 (The value deleted at index -3)