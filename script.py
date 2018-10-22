
import os
import csv
import pandas as pd 
import matplotlib.pyplot as plt
import twython
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer

#run this only the first time or if you don't have things already installed
#nltk.download('punkt')
#nltk.download('stopwords')


#TODO: filter out instrumentals
#TODO: stem data
#TODO: replace album folder shit with a dictionary??

#set general path for folder of albums and any graphs 
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
custom = ['?','(', ')', '.', '[', ']', "'s", "'ll", 'ca'] #add stuff accordingly
stop_words.extend(custom)

#tokenize,filter, and convert lyrics to lowercase
def clean_lyrics(album_folder):

	filtered_lyrics = []
	complete_album = []

	for root, dirs, files in os.walk(data_path + album_folder, topdown = False):
		for name in files:
			if name != '.DS_Store': #prints .DS_Store sometimes for no reason, stop that
		
				#open each file in the specific album folder
				content = open(data_path + album_folder + name).read()

				#set all letters to lowercase
				content = content.lower()

				#tokenize the lyrics
				tokenized_lyrics = nltk.word_tokenize(content)

				#filter the tokenized lyrics
				filtered_lyrics = [words for words 
				in tokenized_lyrics if not words in stop_words]

				for words in tokenized_lyrics:
					if words not in stop_words:
						filtered_lyrics.append(words)

				#compile each album back into its own list
				for words in filtered_lyrics:

					complete_album.append(words)

	return(complete_album)

#return the top 50 used words in an album
def top_words(album_folder):

	complete_album = clean_lyrics(album_folder)
	fdist = nltk.FreqDist(complete_album)
	return(fdist.most_common(50))

#print out the count of each curse word used in the album
def profanity_count(album_folder):

	print('Profanity count for entire album')
	complete_album = clean_lyrics(album_folder)
	profanity_list = ['fuck', 'fucking', 'shit', 'bitch', 'damn'] #maybe add more?

	print(str(album_folder))
	for words in profanity_list:

		print(words + ': ' + str(complete_album.count(words)))
	print(' ')

'''
#get sentiment analysis of lyrics
def sentiment_analysis(album_folder):

	complete_album = clean_lyrics(album_folder)
	sid = SentimentIntensityAnalyzer()
	sentiment = sid.polarity_scores(complete_album)

	#what the fuck is this??
	print(sentiment)

'''

#vocabulary diversity?


			
clean_lyrics(album_folder1)
top_words(album_folder1)
profanity_count(album_folder1)


