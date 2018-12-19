
import os
import csv
import pandas as pd 
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

#set general path for folders of albums and any graphs 
data_path = ('/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data/')
graph_path = ('/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/graphs/')

#set strings for each album folder
album_folder1 = 'ember_to_inferno/'
album_folder2 = 'trivium_EP/'
album_folder3 = 'ascendancy/'
album_folder4 = 'the_crusade/'
album_folder5 = 'shogun/'
album_folder6 = 'in_waves/'
album_folder7 = 'vengeance_falls/'
album_folder8 = 'silence_in_the_snow/'
album_folder9 = 'the_sin_and_the_sentence/'

album_list = [album_folder1, album_folder2, album_folder3, 
album_folder4, album_folder5, album_folder6,
album_folder7, album_folder8, album_folder9]

#set stop words to english and add some custom ones
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!', '...',
';',"`","'",'"',',', "'s", "'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)

#tokenize, filter, and convert lyrics to lowercase
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

#return the top 30 words used in an album
def top_words(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)
	fdist = nltk.FreqDist(complete_album)

	#create line graph of the top 30 words
	top_words_plot = plt.figure(figsize = (50, 20))
	plt.title("Top Words used in " + album_name)
	fdist.plot(30, cumulative = False)
	top_words_plot.savefig(graph_path + 'top_words_' + album_name)

#print out the count of each curse word used in the album
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

#get sentiment analysis of lyrics
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

#print a percentage stating the lexical diversity of an album
def lexical_diversity(album_folder):

	album_name = str(album_folder).replace('/', '')
	complete_album = clean_data(album_folder)

	#divide the number of unique words by the total amount of words
	#multiply by 100 to get a proper percentage
	lexical_diversity = 100 * (len(set(complete_album)) / len(complete_album)) 

	print("Lexical diversity of " + album_name + ':')
	print(lexical_diversity)
	print(' ')
	
#call all functions for each album
top_words(album_folder1)
top_words(album_folder2)
top_words(album_folder3)
top_words(album_folder4)
top_words(album_folder5)
top_words(album_folder6)
top_words(album_folder7)
top_words(album_folder8)
top_words(album_folder9)

profanity_count(album_folder1)
profanity_count(album_folder2)
profanity_count(album_folder3)
profanity_count(album_folder4)
profanity_count(album_folder5)
profanity_count(album_folder6)
profanity_count(album_folder7)
profanity_count(album_folder8)
profanity_count(album_folder9)

sentiment_analysis(album_folder1)
sentiment_analysis(album_folder2)
sentiment_analysis(album_folder3)
sentiment_analysis(album_folder4)
sentiment_analysis(album_folder5)
sentiment_analysis(album_folder6)
sentiment_analysis(album_folder7)
sentiment_analysis(album_folder8)
sentiment_analysis(album_folder9)

lexical_diversity(album_folder1)
lexical_diversity(album_folder2)
lexical_diversity(album_folder3)
lexical_diversity(album_folder4)
lexical_diversity(album_folder5)
lexical_diversity(album_folder6)
lexical_diversity(album_folder7)
lexical_diversity(album_folder8)
lexical_diversity(album_folder9)
