#Immutable types - int , float, other datatypes
a = 10
a = a + 1   # creates NEW value
#Mutable - list, dict , set 
nums = [1, 2, 3]
nums.append(4)   # same object is modified
a = [1, 2, 3]
b = a
b.append(4)
print(a)

#output - [1, 2, 3, 4]
