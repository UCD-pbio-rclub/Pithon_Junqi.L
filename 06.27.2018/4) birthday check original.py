import time 
start_time = time.time ()

birthday_dictionary = {'Rick Sanchez': '01/01/1948', 'Morty Smith': '01/02/2004', 'Summer Smith': '01/03/1996', 'Beth Smith': '01/04/1966', 'Jerry Smith': '01/04/1966'} # Keys must be unique
print ('Welcome to the birthday dictionary. We know the birthdays of:')

name_list = list (birthday_dictionary) # You can also use dictionary.get (key, 'default') to return the value for the key, or default if the key is not there

for x in range (len (name_list)):
    print (name_list [x])

name_asked = input ("Who's birthday do you want to look up? ")
if name_asked in birthday_dictionary: 
    print (name_asked + "'s'birthday is " + birthday_dictionary [name_asked])
else: 
    print ('Sorry, the input name is not in the birthday dictionary.')
    
print ('Your program took', time.time () - start_time, 'seconds to run')
