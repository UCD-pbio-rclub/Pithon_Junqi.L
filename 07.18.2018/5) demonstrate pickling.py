from Organism import *
import pickle

cuscuta = Organism ('Plantae', 'Angiosperms-Eudicots-Asterids', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'C. pentagona', 'Dodder')

kingdom = cuscuta.kingdom
species = cuscuta.species

# Save a variable into a pickle file.
file = open ('C:/Users/louie/Desktop/mylist.pickle', 'wb')
pickle.dump ([kingdom, species], file)
file.close ()

# Get the info back from a pickle file 
with open('C:/Users/louie/Desktop/mylist.pickle', 'rb') as pickle_file:
    content = pickle.load(pickle_file)
print (content)
