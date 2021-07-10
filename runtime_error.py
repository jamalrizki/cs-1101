x=1

def error(x):
    if x > 0:
        print(x)
        error(x + 1)

error(x)
