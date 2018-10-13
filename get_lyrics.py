
import requests
from bs4 import BeautifulSoup

#get lyrics from genius.com
#open a text file that we can print the lyrics onto later
data_path = '/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data/in_waves/'
file_name = 'slave_new_world.txt'
text_file = open(data_path + file_name, 'wb')

#scrape genius.com for whatever song you're looking for
URL = 'https://genius.com/Trivium-slave-new-world-lyrics'
page = requests.get(URL)
html = BeautifulSoup(page.text, 'html.parser')
lyrics = html.find('div', class_= 'lyrics').get_text().encode('ascii', 'ignore')

#write lyrics onto the text file
text_file.write(lyrics)
text_file.close()

print('done')