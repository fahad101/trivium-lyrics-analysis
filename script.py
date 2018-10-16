
import os
import glob
import csv
import pandas as pd 
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#run this only the first time or if you don't have punkt already installed
#nltk.download('punkt')

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


#TODO: clean this up. maybe one neat function??
for root, dirs, files in os.walk(data_path + album_folder1, topdown = False):
	for name in files:
		if name != '.DS_Store': #prints .DS_Store sometimes for no reason, stop that
			#print(os.path.join(name))

			content = open(data_path + album_folder1 + name).read()
			tokens = nltk.word_tokenize(content)

			print(tokens)












