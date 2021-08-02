print('#example1')
a = ('id','date','series','show')
b = ('1234','25-02-20','my_series','my_show')

for obj in zip(a,b):
    print(obj)
    print(type(obj))

print('')
print('#example2')
olympic_finals = ['Grace', 'Jonelle', 'Sinead', 'Ellen', 'Dawn']


for i, olympic_finals in enumerate(olympic_finals, 1):
    b = str(i), olympic_finals
    print(type(b))
    print (b)

print('')
print('#example3')
a = {'id': '1234','date':'25-02-20','series': '3', 'show': 'my_show'}
new_list = list(a.items())
print(new_list)
print(type(new_list[1]))
for i,j in new_list:
     print(f'key= {i} || value= {j}')

