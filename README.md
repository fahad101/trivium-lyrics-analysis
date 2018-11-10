Trivium Lyrics Analysis
===

Description
---

Trivium is an American heavy metal band originatiing from Orlando, Florida. Since their inception in 1999, they have released eight studio albums and one EP. This program is a statistical analysis of the lyrical content of trivium's discography using natural language processing and the [Natural Language Toolkit (NLTK)](https://www.nltk.org/).

Getting the lyrics
---

To begin, I used the `BeautifulSoup` library to web scrape lyrics off of[genius.com](https://genius.com/artists/Trivium). The lyrics for each song were then written onto .txt files. The .txt files were then organized by album. 

```python

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

```

Yes, I am aware that there were more effecient ways to go about this. I decided to go this sloppy route since there weren't that many songs to get and because the focus of this project was the analysis of lyrics and not how to obtain them. A quick search will probably produce other better methods for this.

Analysis
---

For the actual lyrics analysis I used the NLTK paltform since it specializes in working with human language data. The first function `clean_data()` is used to clean and tokenize the raw data. To clean the lyrics, I removed stopwords, punctuation, set all words to lowercase, and removed isntrumental tracks. Finally, the filtered lyrics were tokenized, or split into a list of strings. Each album was split by words.   



Sources and Helpful Links
---
https://en.wikipedia.org/wiki/Trivium_(band)
https://en.wikipedia.org/wiki/Trivium_discography
https://genius.com/artists/Trivium
https://www.nltk.org/
[Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc](https://www.nltk.org/book/)
















