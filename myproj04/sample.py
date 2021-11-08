# 기초 데이터로서 멜론 top100 리스트 구성하기

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

"""
1.방탄소년단의 곡명만 출력해 보세요.
"""
for bts in song_list:
    if bts["artist"] == "방탄소년단":
        print(bts["title"])

"""
2.곡명에 "가을"이 들어가는 곡명만 출력해보세요.
"""
for fall in song_list:
    if "가을" in fall["title"]:
        print(fall["title"])


"""
3.좋아요 수가 200_000이 넘는 곡수는?
"""
result = 0
for like in song_list:
    if like["like"] > 200000:
        result += 1
print(result)

"""
4.가수 별 곡수를 출력해보세요.
(모르겠습니다.)
"""
count = {}
for song in song_list:
    try:
        count[song] += 1
    except:
        count[song] = 1
print(count)
