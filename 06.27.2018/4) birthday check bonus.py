import time 
start_time = time.time ()

birthday_dictionary = {'Rick Sanchez': '01/01/1948', 'Morty Smith': '01/02/2004', 'Summer Smith': '01/03/1996', 'Beth Smith': '01/04/1966', 'Jerry Smith': '01/04/1966'} # Keys must be unique
print ('Welcome to the birthday dictionary. We know the birthdays of:')

name_list = list (birthday_dictionary)

for x in range (len (name_list)):
    print (name_list [x])

birthday_asked = input ("What birthday ??/??/???? do you want to look up? ")
birthday_list = list (birthday_dictionary.values())

if birthday_asked in birthday_list:
    print ('The following people have this birthday:')
    
    for x in range (len (birthday_list)):
        if birthday_asked == birthday_list [x]: 
            print (name_list [x])
        else:
            pass 
else: 
    print ('Nobody in the birthday dictionary has the input birthday.')

print ('Your program took', time.time () - start_time, 'seconds to run')
