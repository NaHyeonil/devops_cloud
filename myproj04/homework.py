import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

for fall in song_list:
    if fall["title"] in "가을":
        print(fall["title"])
