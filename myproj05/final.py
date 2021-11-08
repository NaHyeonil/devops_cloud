"""
"방탄소년단" 곡명만 출력하기
곡명에 "사랑"이 포함된 곡명만 출력하기
"좋아요" 수가 200,000 이상인 곡명만 출력하기
"""

from typing import List  # type hinting
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""

# title_list: list[str] = []
# for song_dict in song_list:
#     title_list.append(song_dict["title"])


title_list: list[str] = []
for song_dict in song_list:
    title: str = song_dict["title"]
    title_list.append(title)
print(title_list)
