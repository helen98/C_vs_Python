x = 1
y = 2

print("x is {}".format(x))
print("y is {}".format(y))
print("Swapping...")
tmp = x # or just x, y = y, x (to swap two at once)
x = y # or (x, y) = (y, x)
y = tmp
print("Swapped.")
print("x is {}".format(x))
print("y is {}".format(y))

# notice, that a function can return more than one value
# a, b, c, d = foo()