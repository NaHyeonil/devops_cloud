const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

// TODO: 현재 timestamp
begin_timestamp = new Date().getTime();
// TODO: shuffle
function shuffle(animal_names) {
    for (let index = animal_names.length - 1; index > 0; index--) {
        const randomPosition = Math.floor(Math.random() * (index + 1));
        const temporary = animal_names[index]; animal_names[index] = animal_names[randomPosition];
        animal_names[randomPosition] = temporary;
    }
}
// TODO: slicing

// TODO: input 받기
//   readline-sync 라이브러리를 설치
//   소스코드가 있는 폴더까지 이동해서 !!!
//   npm install readline-sync


const { question } = require("readline-sync");



end_timestamp = new Date().getTime();

timestamp = end_timestamp - begin_timestamp
// string

const number = question("Enter a number : ");
console.log(number);
console.log(`총${timestamp}초가 걸리셨어요`)
