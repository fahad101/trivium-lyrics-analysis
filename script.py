
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

'''

#create csv file
with open('data.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', 
		quoting = csv.QUOTE_MINIMAL)

	#insert column names
	filewriter.writerow(['song_title', 'album_title', 'lyrics'])

#enter genius.com API credentials
CLIENT_ID = '17Iaiy-KBEY138d1DPsRD6dsyXH_jBv2y2zdRQMGYaRopNEZP2hMv3eO2nQVV9da'
CLIENT_SECRET = 'KSTLyte_6ld2bv5DRz4sLN5VlmW7mcsS77TNvpXyt6pu2Dq_4DdGs0wOyTz5f57ZowF8cOQhuGBdJMi63ftrTg'
TOKEN = 'vyUAzjXiRTAidZoYjh7rznIG4GBTzA7vrW4zZtL-sC5Bz_RuoaiTs_c2d0SFviZk'

#enter other constants
BASE_URL = 'https://api.genius.com/'
ARTIST_NAME = 'Trivium'

#function for getting song title, album title, and lyrics from genius
def get_info(BASE_URL, ARTIST_NAME):

	headers = {'Authorization': TOKEN}
	SEARCH_URL = BASE_URL + '/search'
	song_title = 'Endless Night'
	data = {'q': song_title}
	response = requests.get(SEARCH_URL, params = data, headers = headers)

	return response
	



print('done')
'''






'''
#function or scraping lyrics and 
#writing it onto the .csv file
def scrape_lyrics(SEARCH_URL):

	page = requests.get(SEARCH_URL)
	html = BeautifulSoup(page.text, 'html.parser')
	lyrics = html.find('div', class_='lyrics').get_text().encode('ascii', 'ignore')

	filewriter.writecolumn(lyrics)


'''


df = pd.read_csv('/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data.csv')





print(df.to_string())