//Электронные часы - 1
//Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.
//
//Входные данные
//
//Вводится целое число n.
//
//Выходные данные
//
//Выведите ответ на задачу.
//
//Sample Input:
//
//150
//Sample Output:
//
//2 30

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    n = +n1;

    var rem = getRem(n);
    var hour = getHour(rem);
    var min = getMin(rem)

    console.log(`${hour} ${min}`);
});

function getMin(min){
    return min % 60;
}

function getHour(min){
    return Number.parseInt(min / 60);
}

function getRem(n){
    return n % (24*60);
}