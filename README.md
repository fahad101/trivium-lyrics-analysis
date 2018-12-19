Trivium Lyrics Analysis
===

Description
---

Trivium is an American heavy metal band originating from Orlando, Florida. Since their inception in 1999, they have released eight studio albums and one EP. This program is a statistical analysis of the lyrical content of Trivium's discography using natural language processing and the [Natural Language Toolkit (NLTK)](https://www.nltk.org/). Check out [my article](https://medium.com/@hernanrazo/trivium-lyrics-analysis-using-nltk-53c37a5bd1c8) on Medium for more information and backstory.

Getting the lyrics
---

To begin, I used the `BeautifulSoup` library to web scrape lyrics off of[genius.com](https://genius.com/artists/Trivium). The lyrics for each song were then written onto their own .txt files. The .txt files were then organized by album. 

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

At first, I was going to place all lyrics into a single .csv file but that method felt ineficient and cumbersome. I later decided to just place each song into its own .txt file and organize them with folders. This worked much better.  

Yes, I am aware that there are more effecient ways to go about this. I decided to go this sloppy route since there weren't that many songs to get and because the focus of this project was the analysis of lyrics and not how to obtain them. A quick search will probably produce other better methods.  

Code Explanation
---

For the actual lyrics analysis I used the NLTK platform since it specializes in working with human language data. The first function `clean_data()` is used to clean and tokenize the raw data. To clean the lyrics, I removed stopwords, punctuation, set all words to lowercase, and removed instrumental tracks. Finally, the filtered lyrics were tokenized, or split into a list of strings. Each album was split by words. This function returns an individual album as a long list of strings. 

As you can see, I added a few custom stopwords for this specific project.
```python
#set stop words to english and add some custom ones
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!', '...',
';',"`","'",'"',',', "'s", "'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)

```

```python
#tokenize,filter, and convert lyrics to lowercase
def clean_data(album_folder):

	filtered_lyrics = []
	complete_album = []

	for root, dirs, files in os.walk(data_path + album_folder, topdown = False):
		for name in files:

			#don't include .DS_store
			if name != '.DS_Store': 
		
				#open each file in the specific album folder
				content = open(data_path + album_folder + name).read()

				#set all letters to lowercase
				content = content.lower()

				#tokenize the lyrics
				tokenized_lyrics = nltk.word_tokenize(content)

				#filter the tokenized lyrics of stop words 
				#and instrumental songs
				filtered_lyrics = [words for words 
				in tokenized_lyrics if not words in stop_words]

				for words in tokenized_lyrics:
					if words not in stop_words:
						if words != 'instrumental':
							filtered_lyrics.append(words)

				#compile each album back into its own list
				for words in filtered_lyrics:

					complete_album.append(words)

	return(complete_album)
```

The next three functions actually return analytical data. The first one is `top_words()`. This function returns a distribution plot of the top 30 used words in an album.

```python 
def top_words(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)
	fdist = nltk.FreqDist(complete_album)

	#create line graph of the top 30 words
	top_words_plot = plt.figure(figsize = (50, 20))
	plt.title("Top Words used in " + album_name)
	fdist.plot(30, cumulative = False)
	top_words_plot.savefig(graph_path + 'top_words_' + album_name)
```

The `profanity_count()` function iterates through the album lyrics list and prints a count of each of the curse words used. The specific words I looked for were `fuck`, `fucking`, `shit`, `bitch`, and `damn`.

```python 
def profanity_count(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)
	profanity_list = ['fuck', 'fucking', 'shit', 'bitch', 'damn']

	print('Profanity count for ' + album_name)
	
	#iterate through tokenized lyrics, searching for the curse 
	#words specified in profanity_list
	for words in profanity_list:

		#print results onto the terminal
		print('{0}: {1}'.format(words, str(complete_album.count(words))))
	print(' ')

```

The `sentiment_analysis()` function prints out various sentiment analysis values of an album. For this I used [VADER](https://github.com/cjhutto/vaderSentiment). VADER is a tool used to get various sentiment analysis data from text. The first three values, `neg`, `neu`, and `pos` give a proportion of the text that counts as negative, neutral, and positive, respectively. The final value `compound` is the sum of the first three and standardized to give an overall postivie or negative score between -1 and 1.  

To get these scores, the original tokenized lyrics get combined into one new giant string, separating each word by a space. This new string is passed to the local instance of the `SentimentIntensityAnalyzer()` class.

```python
def sentiment_analysis(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)
	sid = SentimentIntensityAnalyzer()
	seperator = ' '

	#combine all lyrics into one giant string
	#seperating all words with spaces
	lyrics_string = seperator.join(complete_album)

	#get polarity score for giant string
	sentiment = sid.polarity_scores(lyrics_string)	

	#print results onto the terminal
	print("Sentiment Analysis for " + album_name)
	print(sentiment)
	print(' ')
```

The final function `lexical_diversity()` prints out the lexical diversity of each album. Lexical diversity is a ratio of the unique words to the total number of words in a text. Using the built-in functions `set()`, and `len()`, the function counts the unique instances of any words in the album's lyrics. As stated earlier, this is then divided by the total words in the album. The function then multiplies the result by 100 to get a clean percentage. 

```python
def lexical_diversity(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)

	#divide the number of unique words by the total amount of words
	#multipy by 100 to get a proper percentage
	lexical_diversity = 100 * (len(set(complete_album)) / len(complete_album)) 

	print("Lexical diversity of " + album_name + ':')
	print(lexical_diversity)
	print(' ')

```

Results
---

As a longtime Trivium fan, the results I got from this project were not as exciting as I thought they would be. Maybe it's because I was already so familiar with the lyrics just by regular consuption of their music. 

The charts obtained from the `top_words()` function are shown below. Unsurprisingly, a lot of the words that have large occurances are those that are part of chorus sections. Many of these words also have negative connotations, which as shown later, affected the sentiment analysis. For Ascendancy specifically, I found it kind of funny how the long segment of "heys" in A Gunshot to the Head of Trepidation did not make it the number one most used word on the album. 

![ember_to_inferno_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_ember_to_inferno.png)  

![trivium_ep_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_trivium_EP.png)  

![ascendancy_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_ascendancy.png)  

![crusade_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_the_crusade.png)  

![shogun](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_shogun.png)  

![in_waves_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_in_waves.png)  

![vengeance_falls_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_vengeance_falls.png)  

![silence_in_the_snow_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_silence_in_the_snow.png)  

![sin_and_the_sentence_dist](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/graphs/top_words_the_sin_and_the_sentence.png)  
 
The results for the `profanity_count()` function show that most albums are not heavily explicit. The most explicit album is Ascendancy with Shogun at a close second. This makes sense since they both have "fuck" or "fucking" in their top words as well. Having Ascendancy come out as being the most profane comes as a surprise since only three of its songs have curse words in them (Washing Away Me in the Tides, Departure, and Declaration). Shogun has almost all of its songs include some curse words in them. Albums like In Waves, Vengeance Falls, and Trivium EP have no profanity at all. 

![prof_count1](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/terminal_screenshots/prof_count1.png)

![prof_count2](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/terminal_screenshots/prof_count2.png)

For the `sentiment_analysis()` function, I kind of already knew that it would return fairly negative results. Trivium's lyrics are not exactly the most happy or optimistic. What stood out to me most was how close all the albums came out to be. The most negative albums are The Crusade and Shogun, even if it's not by much.

![sentiment_screenshot](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/terminal_screenshots/sent_analysis_results.png)

The results from the `lexical_diversity()` function were probably the results that surprised me the most. They all came out to having fairly similar scores for this too. The album Trivium EP came out with the highest score but I suspect this is because it has significantly less songs than the rest of the albums. I personally thought Shogun would have the highest score because the lyrics mention many characters and references from Greek mythology. I figured this would have diversified the corpus quite a bit. The structure of the songs in this album also differ greatly from the rest in my opinion, which is also why I thought it would have gotten a higher score. 

![lex_div](https://github.com/hrazo7/trivium-lyrics-analysis/blob/master/terminal_screenshots/lex_div_results.png)

The data obtained from this project was a bit bland and underwhelming but I did learn a lot of new things in the process. Maybe if I had chosen an artist with more albums I would have gotten more data to work with or if I extend this project to analyze specific songs there would be more to show. In the end, this was more of a project to get started on natural language processing and NLTK. I am still a Trivium fan and look forward to perhaps updating this project when they release more music in the future.

Sources and Helpful Links
---
https://en.wikipedia.org/wiki/Trivium_(band)  
https://en.wikipedia.org/wiki/Trivium_discography  
https://genius.com/artists/Trivium  
https://www.nltk.org/  
[Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc](https://www.nltk.org/book/)  
[Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.](https://github.com/cjhutto/vaderSentiment)  



