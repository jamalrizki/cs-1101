alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

def has_duplicates(a):
   a= histogram(a)
   for i in a:
     b=(a[i])
     if b > 1:
        return True
   else:
        return False

def test(a):
     for i in a:
        f = has_duplicates(i)
        if f == True:
           print(f'{i} has duplicates')
        else:
           print(f'{i} has no duplicates')

test(test_dups)


     
           





