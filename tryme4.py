def new_line(): # 1 line
	print('.')

def three_lines(): # nest new line in three lines 
        new_line()
        new_line()
        new_line()

def nine_lines(): # nest 3 lines in 9 lines 
        three_lines()
        three_lines()
        three_lines()

def clear_screen(): # combine functions to create 25 lines
        nine_lines()
        nine_lines()
        three_lines()
        three_lines()
        new_line()

print("##### 9 lines")
nine_lines()
print("##### 25 lines")
clear_screen()

