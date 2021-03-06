const numbers = [1, 2, 3, 4, 5]; // [31, 89, 24, 81, 46];

// Array의 sort
function make_random_value(number1, number2) {
    return Math.random();
}

const number1 = numbers.map(
    (number) => ({ number, 기준값: Math.random() }),
);

const number2 = number1.sort(
    (value1, value2) => {
        return value1.기준값 - value2.기준값;
    }
);

const number3 = number2.map(
    (value) => value.number
);

console.log(new_numbers);


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

begin_timestamp = new Date().getTime();

function shuffle(animal_names) {
    for (let index = animal_names.length - 1; index > 0; index--) {
        const randomPosition = Math.floor(Math.random() * (index + 1));
        const temporary = animal_names[index]; animal_names[index] = animal_names[randomPosition];
        animal_names[randomPosition] = temporary;
    }
}

shuffle(animal_names);

let success_counter = 0;

const random_name = animal_names.slice(0, 5);

for (i = 0; i < random_name.length; i++) {
    console.log(random_name[i]);
    const { question } = require("readline-sync");
    const name = question(">>> ")
    if (name == random_name[i]) {
        success_counter += 1;
        console.log("정답!")
    } else {
        console.log("실패!")
    }
}

end_timestamp = new Date().getTime();

timestamp = (end_timestamp - begin_timestamp) / 1000

console.log(`${success_counter}번 성공`)
console.log(`총${timestamp}초 소요`)