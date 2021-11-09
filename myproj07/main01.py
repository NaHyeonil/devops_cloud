"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 리스트를 만들어봅시다.
 - 단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 좋아요 수로 TOP10 곡명 리스트를 만들어봅시다.
