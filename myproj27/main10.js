const { melon_data: song_array } = require("./melon_data");

Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
};


const result = song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"
    )
    // .reduce((acc, { like }) => acc + like, 0);
    .map(({ like }) => like)
    .sum();

console.log("result :", result);









// const like_total = song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, song) => acc + song.like, 0);


// console.log(`좋아요 총 합 : ${like_total}`);