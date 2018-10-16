
import os
import csv
import pandas as pd 
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#run this only the first time or if you don't have things already installed
nltk.download('punkt')
nltk.download('stopwords')

#set general path for folder of albums
data_path = ('/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data/')

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

#set stop words to english
stop_words = set(stopwords.words('english'))

#tokenize and filter lyrics
def tokenize_and_filter(album_folder):

	for root, dirs, files in os.walk(data_path + album_folder, topdown = False):
		
		for name in files:

			if name != '.DS_Store': #prints .DS_Store sometimes for no reason, stop that
		
				#open each file in the specific album folder
				content = open(data_path + album_folder + name).read()

				#tokenize the lyrics
				tokenized_lyrics = nltk.word_tokenize(content)

				#filter the tokenized lyrics
				filtered_lyrics = [words for words 
				in tokenized_lyrics if not words in stop_words]

				filtered_lyrics = []

				for words in tokenized_lyrics:
					if words not in stop_words:
						filtered_lyrics.append(words)

				#print(tokenized_lyrics) #TODO: use this later for lyric generation??
				return(filtered_lyrics)
				print('lyrics tokenized and filtered')

#tokenize lyrics
tokenize_and_filter(album_folder1) #ember to inferno
tokenize_and_filter(album_folder2) #trivium EP
tokenize_and_filter(album_folder3) #ascendancy
tokenize_and_filter(album_folder4) #the crusade
tokenize_and_filter(album_folder5) #shogun
tokenize_and_filter(album_folder6) #in waves
tokenize_and_filter(album_folder7) #vengeance falls
tokenize_and_filter(album_folder8) #silence in the snow
tokenize_and_filter(album_folder9) #the sin and the sentence 
