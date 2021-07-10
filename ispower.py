def is_divisible(a, b):
    return a % b == 0
    
def is_power(a, b):
    if not is_divisible(a, b):
        return False
    if a == b:
        return True
    if b == 1:
        return False
    else:
        a = a/b
        b = b
    return is_power(a, b)

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
