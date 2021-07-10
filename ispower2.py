def is_divisible(a, b):
    return a % b == 0
    
def is_power(a, b):
    #check to see if divisable with an if/else statement
    if is_divisible(a, b):
        # base case if arguments are equal
        if a == b:
            return True
        # base case if second argument is equal to one
        if b == 1:
            return False
        #recursive function 
        else:
            #re initializing variables a and b
            a = a/b
            b = b
            #recursively calling is_power
            return is_power(a, b)
    else:
        return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
