# Generators

# infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# DON'T RUN THIS!
for i in infinite_sequence():
    print(i, end=" ")

# Use Interpreter and next() to test an infinite sequence

# Generator Expressions

nums_squared_lc = [num**2 for num in range(5)] # [0, 1, 4, 9, 16]
nums_squared_gc = (num**2 for num in range(5)) # <generator object <genexpr> at 0x107fbbc78>
