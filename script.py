import csv
import pandas as pd

df = pd.read_csv('/Users/hernanrazo/pythonProjects/trivium_lyrics_analysis/data.csv', encoding = 'latin-1')


print(df.to_string())