a = [1, 2, 3]
b = a

c = [1, 2, 3]
d = [1, 2, 3]

print( a is b) # True
print(a is c) # False
print(c is d) # False

print(a == c) # True
print(c == d) # True
