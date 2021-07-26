#these values are both equivalent and identical as the
#value refers to the content of the string

value1 = "hello world"
value2 = "hello world"

print(value1 is value2) #output = True

#these objects are equivalent but not identical as the value is a list
obj1 = ["hello world"]
obj2 = ["hello world"]

print(obj1 is obj2) #output = false

# obj3 is now referencing obj1 this mean now means the object is aliased
obj3 = obj1

print(obj3 is obj1) #output = true

# we can check this as lists are mutable

obj3.append("world hello")

print(obj3)
print(obj1)

#as we can see object 3 is referencing obj1
#output = ['hello world', 'world hello'] fot both

#myfunction
#this function will create a flattend list

nest = [1, 2, [3,4], 5] #initial nested object
argument = nest #this is a new variable that references nest creating an alias
                # it will also be the argument that is passed to myfunction

def my_function(parameter): #declaring the parameter as parameter
    newlist = [] # creating new list
    for i in parameter: #a for loop over the list
        if type(i) == list: #a check to see the objects value
            for j in i: #a for loop over the nested list
                newlist.append(j)  #pushing nested list to the array
        else:
            newlist.append(i) #pushing un-nested list to the array
    return newlist

print("output:" +" " + str(my_function(argument))) #output = output: [1, 2, 3, 4, 5] 
