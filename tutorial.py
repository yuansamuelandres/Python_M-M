# In the name of Allah

''' #022: List Methods I '''
# Appending
myFriends = ["Ahmad", "Paul", False]
myFriends.append("Mazen")
print(myFriends) # ['Ahmad', 'Paul', False, 'Mazen']

# Extending
nums = ["one", "two"]
no = [1, 2, 3]
nums.append(no)
print(nums) # ['one', 'two', [1, 2, 3]]
nums.extend(no)
print(nums) # ['one', 'two', [1, 2, 3], 1, 2, 3]

# Removing (Only the first encountered element)
myFriends.remove("Paul")

# Sorting (Numbers Only || Strings Only)
y = [1, 998, -19, 0]
y.sort() # Default: reverse=False 
print(y) # [-19, 0, 1, 998]
y.sort(reverse=True)
print(y) # [998, 1, 0, -19]

x = ['A', 'Y', 'M']
x.sort()
print(x) # ['A', 'M', 'Y']

# Reversing (Only reversing the list)
z = [ 10, 1, "Zero", 556, 7657, "Osama"]
z.reverse()
print(z) # ['Osama', 7657, 556, 'Zero', 1, 10]