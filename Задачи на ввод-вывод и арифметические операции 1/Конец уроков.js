//Конец уроков
//В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут. Определите, когда заканчивается указанный урок.
//
//Входные данные
//
//Дан номер урока (число от 1 до 10).
//
//Выходные данные
//
//Выведите два целых числа: время окончания урока в часах и минутах. При решении этой задачи нельзя пользоваться циклами и условными инструкциями.
//
//Sample Input:
//
//3
//Sample Output:
//
//11 35

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    n = +n1;

    var allMin = getAllMin(n);
    var hour = 9 + getHour(allMin);
    var min = getMin(allMin)

    console.log(`${hour} ${min}`);
});

function getAllMin(n){
    return n * 45 + (n - 1) * 5 + Number.parseInt((n - 1) / 2) * 10;
}

function getHour(min){
    return Number.parseInt(min / 60);
}

function getMin(allMin){
    return allMin % 60;
}