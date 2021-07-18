# 1

def any_lowercase1(s):
     for c in s:
          print(c)
          if c.islower():
               return True
          else:
               return False



# 2

def any_lowercase2(s):
     for c in s:
          print(c)
          if 'c'.islower():
               return 'True'
          else:
               return 'False'


# 3

def any_lowercase3(s):
     for c in s:
          print(c)
          flag = c.islower()
     return flag


# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          print(c)
          flag = flag or c.islower()
     return flag


# 5

def any_lowercase5(s):
     for c in s:
          print(c)
          if not c.islower():
               return False
     return True


any_lowercase1("other")
any_lowercase1("OTHER")
any_lowercase2("other")
any_lowercase2("OTHER")
any_lowercase3("other")
any_lowercase3("OTHER")
any_lowercase4("other")
any_lowercase4("OTHER")
any_lowercase5("other")
any_lowercase5("OTHER")

