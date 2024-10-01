def  apply_function(func, value):
    return func(value)

def square(x):
    return x * x

def double(x):
    return x + x

print(apply_function(square, 5))
print(apply_function(double, 5))