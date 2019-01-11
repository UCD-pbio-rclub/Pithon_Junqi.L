# Determine which day of the week is today. 
import datetime # Return the day of the week as an integer: Monday (=0), Tuesday (=1), Wednesday (=2), Thursday (=3), Friday (=4), Saturday (=5), Sunday (=6)

# Scrape that day's menu
import requests #For request to the website
from bs4 import BeautifulSoup  #For parsering

# Return google image searching result
import urllib.request
import json

# Construct the HTML 
import dominate
from dominate import document
from dominate.tags import *

# Send emails
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def day(): # Determine which number of the tab should use for that day's menu 
    day_num = datetime.datetime.today().weekday()
    if day_num == 6: # If it's a Sunday (=6) [Sunday is treated differently here because it's special]
        day_DC = 1 # It's the 1st day of a week, so DC regards it as the 1st day of a week → tab 1
    else: 
        day_DC = day_num + 2 # The returned number from datetime module and the DC's tab number have a difference of 2 for all the days in a week except Sunday. For example, the datetime will return Friday as 4, but DC uses tab 6 for Friday
    return day_DC

def requests_beautiful_soup(url): # Convert a url into a BeautifulSoup instance 
    page = requests.get(url)
    if page.status_code != 200: # Other response codes, such as 404, mean an error 
        return page.raise_for_status() # Indicate specific error type
    else: # <Response [200]> means normal
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify()) # Check briefly the content of the soup 
        return soup

def scrape_main_content(input_soup, day): # Find the main_content from the input_soup based on the number for the day in DC
    main_content = input_soup.find('div', attrs = {'id': 'tab'+str(day)+'content'}) # All the info you need for that day is in the tab#content
    return main_content

def meal_day(major_content): # Return the meals from the major_content based on the number for the day in DC
    meal_tag = major_content.find_all('h4')
    
    meal_list = []
    for meal in meal_tag: 
        meal_name = meal.text
        meal_list.append(meal_name)
    return meal_list

def meal_dict(meal_today, major_content): # Return a dictionary of {meal:[dish_names]}
    meal_dict = {}
    for meal_pick in meal_today: 
        dish_list = major_content.find('h4',text=str(meal_pick)).find_next_siblings('ul')
        
        real_dish_list = []
        for dish in dish_list: 
            item_list = []
            for item in dish.findChildren('span'):
                item_list.append(item.text)
            real_dish_list += item_list
            
        meal_dict[meal_pick] = real_dish_list
    return meal_dict

def google_img_type_list(dish_name, search_length): # Return a list of [(link for the large original images, type of image)] with a fixed search_length if the dish name is searchable and the url of the google image searching page → It returns 2 values. Otherwise, it returns ['The dish name has weird letters that cannot be searched directly.']
    # Try/Except deals with some weird letters in the dish names that prohibit the searching
    try: 
        query = '+'.join(dish_name.split())
        
        # Provide url & header for get_soup()
        url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
        # print ('>>> Base searching page from Google image:', url)
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        
        soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

        ActualImages = [] # ActualImages contains (link for the large original images, type of image) sets
        for a in soup.find_all("div",{"class":"rg_meta"}):
            img_link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            ActualImages.append((img_link,Type))
            if len(ActualImages) == search_length: # Once your researches the search_length, stop searching to save time because it can store up to 100 images. This if statement circumvent the condition where len(ActualImages) == 0, which will be catched later 
                break 
        
        if len(ActualImages) == 0: # If the search has no result 
            return ['Your search has no return.'], url
        else: 
            return ActualImages[:search_length], url # ActualImages can only obtain the 1st 100 images in the base page; it cannot get more than that. However, I only use the 1st 5 for saving spaces
    except: # If the dish_name has weird letters 
        return ['The dish name has weird letters that cannot be searched directly.'], url

def send_email(email): # email is an HTML
    # Info about sender & receiver email addresses and the password of the sender_email
    sender_email = "butlerpennyworthunfryeggs@gmail.com"
    receiver_email = "louieeye@gmail.com"
    # password = input("Type your password and press enter: ")
    password = '5serveyou' # I don't really care about the testing email address so I stored the password here, although it's unsafe to do this, especially when you're going to share the code with someone

    # Pass info above into the MIMEMultipart("alternative") instance
    message = MIMEMultipart('alternative')
    message['Subject'] = "Today's DC Menu"
    message['From'] = sender_email
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message
    html = email 
    
    # Turn these into html MIMEText objects
    part = MIMEText(html, "html")

    # Add HTML parts to MIMEMultipart message. The email client will try to render the last part first
    message.attach(part)

    # Initiated a secure SMTP connection
    port = 465  # Port 465 is the standard port for SMTP over SSL

    # Create a secure SSL context for secure connection with esrver and send emal 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: # smtp.gmail.com is the SMTP server 
        server.login(sender_email, password)
        # Send email here
        server.sendmail(sender_email, receiver_email, message.as_string())
    # This function returns None 
    
    

def main(): 
    day_DC = day()
    webpage_url = 'https://housing.ucdavis.edu/dining/menus/dining-commons/tercero/' #Defult DC is Tercero 
    
    soup = requests_beautiful_soup(webpage_url)
    content = scrape_main_content(soup, day_DC)
    
    meal_today_list = meal_day(content)
    meal_dictionary = meal_dict(meal_today_list, content)
    
    doc = dominate.document(title='DC Menu')
    
#     with doc.head: # This is for the <style> formatting
#         style("""\
#             * {
#                 box-sizing: border-box;
#             }

#             .column {
#                 float: left;
#                 width: 20%;
#                 padding: 5px;
#             }
#             /* Clearfix (clear floats) */

#             .row::after {
#                 content: "";
#                 clear: both;
#                 display: table;
#             }""")
        
    with doc.head: # This is for the <style> formatting
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')
        style("""\
            body {
                 background-color: #F9F8F1;
                 color: #2C232A;
                 font-family: sans-serif;
                 font-size: 2.6em;
                 margin: 3em 1em;
             }
         """)
        
    with doc:
        h1("Good Morning. Here is Today's DC Menu.")
        
        for meal in meal_dictionary: 
            h2(">>> Today's ", meal, ' has: ',', '.join(meal_dictionary[meal]))
            for dish_name in meal_dictionary[meal]:
                image_list, search_link = google_img_type_list(dish_name, 5) # The search_length is 5 
                a(dish_name,href=search_link)
                with div(_class='row'): 
                    for image_link in image_list: # image_list contains (link for the large original images, type of image) sets
                        div(img(src=image_link[0], alt=image_list[0],style='width:100%'), _class='column') # src=image_link[0] because image_link is a set
                        
    send_email(str(doc))
    print('Done')
    
main()
