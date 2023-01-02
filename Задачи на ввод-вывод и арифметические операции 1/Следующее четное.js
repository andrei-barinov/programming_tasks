//Следующее четное
//Дано целое число n. Выведите следующее за ним четное число. При решении этой задачи нельзя использовать условную инструкцию if и циклы.
//
//Входные данные
//
//Вводится натуральное число.
//
//Выходные данные
//
//Выведите ответ на задачу.
//
//Sample Input:
//
//9
//Sample Output:
//
//10

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    n = parseInt(n1);
    console.log(getResult(n));
});

function getResult(n){
    return n + (2 - n % 2);
}