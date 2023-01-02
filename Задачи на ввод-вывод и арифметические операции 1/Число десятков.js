//Число десятков
//Дано неотрицательное целое число. Найдите число десятков в его десятичной записи (то есть вторую справа цифру его десятичной записи).
//
//Входные данные
//
//Вводится неотрицательное целое число.
//
//Выходные данные
//
//Выведите ответ на задачу.
//
//Sample Input:
//
//123
//Sample Output:
//
//2

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    n = parseInt(n1);
    console.log(calcSecondFigure(n));
});

function calcSecondFigure(n){
    if(Math.abs(n) < 10){
        n = "Число меньше 10";
    }else if(Math.abs(n) < 100){
        n = Math.abs(Number.parseInt(n / 10));
    } else {
        n = Math.abs(Number.parseInt((n % 100) / 10));
    }

    return n;
}