# In the name of Allah

''' #026, #027, #028, #029: Set & Methods '''
# Set items are enclosed in curly braces.
# Set items aren't ordered nor indexed.
# Set indexing & slicing can't be done.
# Set only has immutable data types (not unhashable types)
# Set items are unique.

mine = {"Yuan", 5, True}
print(mine) # {True, 'Yuan', 5}

# Union()
his = {"N", 23, False, 5}
print(his.union(mine))  # {False, True, 'Yuan', 5, 23, 'N'}
theirs = {'G'}
print(his.union(mine, theirs))  # {False, True, 'G', 5, 23, 'Yuan', 'N'}

# Adding
mine.add(22)
print(mine) # {True, 5, 22, 'Yuan'}

# Copying (Shallow Copy)

# Removing (Throws an error if element not found)
his.remove(False)
# his.remove(True)    # Error

# Discarding (Doesn't throw an error if element not found)
his.discard(False)
his.discard(True)   # No error

# Updating
theirs.update(his)
print(theirs)   # {'N', 'G', 23}

# difference()
print(mine.difference(his)) # {'Yuan', True, 5, 22}

# difference_update() (Update the original Set with the difference)
his.difference_update(mine)
print(his)  # {23, 'N'}

# intersection()
print(his.intersection(mine))   # set() 'No intersection'

# intersection_update()
his.intersection_update(mine)
print(his)

# symmetric_difference()
print(theirs)   # {5, 23, 'G', 'N'}
print(mine) # {True, 'Yuan', 5, 22}
print(theirs.symmetric_difference(mine))   # {True, 'Yuan', 'G', 'N', 22, 23}

# symmetric_difference_update()
print(theirs)   # {5, 23, 'G', 'N'}
print(mine) # {True, 'Yuan', 5, 22}
theirs.symmetric_difference_update(mine)
print(theirs)   # {True, 'N', 'G', 'Yuan', 22, 23}

# issuperset()
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True

# issubset()
a = {1, 2, 3}
b = {1, 2}
print(a.issubset(b))    # False

# isdisjoint()
print(b.isdisjoint(a))  # False