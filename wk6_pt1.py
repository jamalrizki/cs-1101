def string(string):
    list1 = string.split()
    del list1[1]
    list1.pop(3)
    list1.remove("assignment")
    list1.sort()
    list1.append('than')
    list1 += ['test']
    list2 = ['again']
    list1.extend(list2)
    space = " "
    string2 = space.join(list1)
    print(string2)


string('hello world i am doing my assignment earlier')


