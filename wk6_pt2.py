nest = [1, 2, [3,4], 5] #nested list example

def no_more_nest(nest):
    newlist = []
    for i in nest:
        if type(i) == list:
            for j in i:
                newlist.append(j)
        else:
            newlist.append(i)
    return newlist

print("nest:" +" " + str(no_more_nest(nest)))

def times(a, b, c): # * operator example
    return a * b / c


nest2 = [1, 2, 3]
print("*:" + " " + str(times(*nest2)))


sliced_list = [1,2,3,4,5,6] # sliced list example
print("sliced:" +" " + str(sliced_list[:3:-1]))

nest += [6,[7,8]] #  += operator example
print("+=:" +" " + str(no_more_nest(nest)))


def filtered_list(n): #  list filter example
    newlist2 = []
    for i in n:
        if type(i) != list:
            newlist2.append(i)
    return newlist2

print("filter:" +" " + str(filtered_list(nest)))

nest.append([9]) #  legal but unexpected result example
print("legal:" +" " + str(nest))



            
