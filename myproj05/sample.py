import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
print(song_list)

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

"""
artist_dict = {}
for song_dict in song_list:
    artist: str = song_dict["artist"]

    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1
    # artist_list.append(artist)

print(artist_dict)

# {
#     "방탄소년단": 10,
#     "소미" : 3,
# }

# artist_list = []
# for song_dict in song_list:
#     artist_list.append(song_dict["artist"])

# List comprehension
artist_list = [song_dict["artist"] for song_dict in song_list]
