
import requests
from bs4 import BeautifulSoup

#get lyrics from genius.com
#open a text file that we can print the lyrics onto later
data_path = 'YOUR_FOLDER_PATH_HERE'
file_name = 'TXT_FILE_NAME_HERE'
text_file = open(data_path + file_name, 'wb')

#scrape genius.com for whatever song you're looking for
URL = 'GENIUS.COM_URL_HERE'
page = requests.get(URL)
html = BeautifulSoup(page.text, 'html.parser')
lyrics = html.find('div', class_= 'lyrics').get_text().encode('ascii', 'ignore')

#write lyrics onto the text file
text_file.write(lyrics)
text_file.close()

print('done')