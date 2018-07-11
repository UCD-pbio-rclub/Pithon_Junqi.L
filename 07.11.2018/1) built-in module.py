# The module I want to demonstrate is json 
import json

import requests
import webbrowser

prof_name = input ('>>> Who do you want to search? ') # You can use Prof David Wilson as an example.
first_last_list = prof_name.split (' ')
first_name, last_name = first_last_list [0], first_last_list [1]

web = 'http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=20&callback=&q=' + first_name + '%20' + last_name + '&defType=edismax&qf=teacherfirstname_t^2000%20teacherlastname_t^2000%20teacherfullname_t^2000%20autosuggest&bf=pow(total_number_of_ratings_i,1.7)&sort=score%20desc&siteName=rmp&group=on&group.field=content_type_s&group.limit=20'
json_page = requests.get (web)

if json_page.status_code != 200:
    warn('Search: {}; Status code: {}. Status of the request is not normal.'.format (search, json_page.status_code))

wjdata = json_page.json()
print ('>>> The following is the original .json file: ')
print (json.dumps(wjdata))

input('>>> Press Enter to see a pretty print of the .json file...')
print ('>>> A pretty print of the .json file: ')
print(json.dumps(wjdata, sort_keys=True, indent=4))

input('>>> Press Enter to open the webpage...')
prof_number = wjdata ['grouped']['content_type_s']['matches']
count = overall_quality = level_of_difficulty = number_of_ratings = 0
if prof_number == 0: # No prof has such a name in the database.
    overall_quality = level_of_difficulty = number_of_ratings = 'No name found.'
else: # At least 1 prof has such a name in the database. 
    prof_list = wjdata ['grouped']['content_type_s']['groups'][0]['doclist']['docs']
    for one_prof in prof_list:
        schoolname = one_prof ['schoolname_s']
        if schoolname != 'University of California Davis': # I only care about the prof at UCD, no matter how many prof have the same name. This line checks the school name inside the json.
            continue
        else:
            count = count + 1
    
        if count != 1: # More than 1 UCD prof has this name.
            # This is not verified since I haven't met any 2 UCD prof who share 1 name. However, it should work.
            overall_quality = level_of_difficulty = number_of_ratings = 'More than 1 prof in UCD.'
        else: # Only 1 UCD prof has this name.
            url_id = one_prof ['pk_id']
            webbrowser.open("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str (url_id))
# Other 3rd party modules are used to scrape out the data...
