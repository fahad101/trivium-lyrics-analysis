
import requests
from bs4 import BeautifulSoup

#get lyrics from genius.com
#open a text file that we can print the lyrics onto later
data_path = '/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data/the_sin_and_the_sentence/'
file_name = 'thrown_into_the_fire.txt'
text_file = open(data_path + file_name, 'wb')

#scrape genius.com for whatever song you're looking for
URL = 'https://genius.com/Trivium-thrown-into-the-fire-lyrics'
page = requests.get(URL)
html = BeautifulSoup(page.text, 'html.parser')
lyrics = html.find('div', class_= 'lyrics').get_text().encode('ascii', 'ignore')

#write lyrics onto the text file
text_file.write(lyrics)
text_file.close()

print('done')