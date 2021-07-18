prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
     if letter == "Q":
         suffix = 'uack'
         print(letter + suffix)
     elif letter == "O":
         suffix = 'uack'
         print(letter + suffix)
         suffix = "ack"
     else:
         print(letter + suffix)
