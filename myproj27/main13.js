const { melon_data: song_array } = require("./melon_data");


// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.


const top_like_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => {
        if (!acc || acc.like < song.like)
            return song;
        return acc;
    }, null);


console.log(top_like_song);