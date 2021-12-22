// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort


//Arrat의 sort는 
//  자신(array)의 순서도 변경하고 자신을 반환
//Python의 List

song_array.sort(
    (song1, song2) => song1.like - song2.like,
);


for (const song of song_array) {
    console.log(song.like, song.title);
}