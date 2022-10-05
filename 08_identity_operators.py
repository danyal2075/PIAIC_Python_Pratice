# these are used to compare the object, it will return true if both are equal means same obejct with same memnory location.
# We use identity operators to compare the memory location of two objects.

x = ["apple", 'banana']
y = ['apple', 'banana']
z = x

print(id(x))
print(id(z))
print(id(y))
print(x is z)
# this will return False because x and y have different memory locations.
print(x is y)