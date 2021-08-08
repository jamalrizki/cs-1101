
a = {} 
with open('f1.txt','r') as a: 
        a = eval(a.read())
        
def write_func(a):
    with open('f.txt','w+') as f: 
            f.write("{\n")
            for k in a.keys(): 
                    f.write(f"'{k}' : {a[k]},\n") 
            f.close()
    with open('f.txt', 'a+') as f:
            f.write("'date':['nov', 'dec'], \n"
            "'station':['jersey', 'Spotify'], \n"
            "'playlist':['new', 'featured'] \n")
            f.write('}')
            f.close()

write_func(a)
test = {} 
with open('f.txt','r') as test: 
        test = eval(test.read()) 

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for i in val:
          if i not in inverse:
            inverse[i] = [key]
          else:
            inverse[i].append(key)
    print(inverse)


invert_dict(test)

