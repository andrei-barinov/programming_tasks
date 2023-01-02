//Последняя цифра
//Дано натуральное число. Выведите его последнюю цифру.
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
//176
//Sample Output:
//
//6

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    n = parseInt(n1);
    console.log(calcLastFigure(n));
});

function calcLastFigure(n){
    return n % 10;
}