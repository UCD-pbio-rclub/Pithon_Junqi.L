import pandas
from pandas import read_csv

# Q1
## Method 1
file = pandas.read_csv('C:/Users/louie/Desktop/sf-civic-art-collection.csv', skiprows=[1]) # Skip the 2nd row (index 1). Both the 1st and the 2nd rows have titles, but the 1st one is more complete than the 2nd one so skip the 2nd one. 

## Method 2 
# file = pandas.read_csv('C:/Users/louie/Desktop/sf-civic-art-collection.csv')
# file = file.drop(0) # Can also drop the 1st row like this



# Q2
## Method 1 
artist_freq_dict = file.artist.value_counts().to_dict() # Count the frequencies of artists and make a dictionary of 'name': frequency
artist_freq_list = [(freq, name) for name, freq in zui_frequent_artist.items()] # Create a list of tuples (frequency, 'name')
artist_freq_list = sorted(artist_freq_list, reverse=True) # Now sort the list
print('The most frequent artist is',artist_freq_list[0][1],'and (s)he has',artist_freq_list[0][0],'paintings.')

## Method 2 
# most_fame_artist_dict = file.artist.value_counts().head(1).to_dict() # Turn the most frequent pair into a dict {'name': frequency}
# print('The most frequent artist is',list(most_fame_artist_dict.keys())[0],'and (s)he has',list(most_fame_artist_dict.values())[0],'paintings.')



# Q3
filter = file[file['artist']==artist_freq_list[0][1]] # Filter out the rows that have the most frequent artist's name in the 'artist' column
portfolio = filter[['title','created_at']] # Create a new DataFrame based on the filter with the 'title' and the 'created_at' columns
print(portfolio)
