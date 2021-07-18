import math
a = 1
def my_sqrt(a):
    x = 10
    while True:
         y = (x + a/x) / 2.0
         if y == x:
              break
         x = y
    return(y)


def test_sqrt(a):
    while a < 26:
        print("a = " + str(a) + " | my_sqrt(a) = " + str(my_sqrt(a)) + " | math.sqrt(a) = " + str(math.sqrt(a)) + " | diff = " + str(abs(my_sqrt(a))-(math.sqrt(a))))
        a = a + 1


test_sqrt(a)
