def num1(num1):
    try:
        f = open(num1, 'r')
        for line in f:
             print(line, end = '')
        f.close()
    except:
        print('This file does not exist')


#num1('txt.txt')


try:
    with open('img.jpg', 'r') as r:
        with open('new_img.jpg','wb') as w:
            for i in r:
                w.write(i)

except:
    with open('img.jpg', 'rb') as r:
        with open('new_img.jpg','wb') as w:
            for i in r:
                w.write(i)

def num2(num2):
    import os
    if os.path.exists("txt1.txt"):
        try:
            f = open("txt1.txt", 'a')
            f.write(num2)
            f.close()
        except:
            print('there was an error editing the file please use the correct format')
    else:
        print('please create a file first')
            

num2("my assignment")

        
