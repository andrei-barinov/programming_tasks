//Сумма цифр
//Дано трехзначное число (оно может быть отрицательным). Найдите сумму его цифр.
//
//Входные данные
//
//Вводится трехзначное число.
//
//Выходные данные
//
//Выведите ответ на задачу.
//
//Sample Input:
//
//192
//Sample Output:
//
//12

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    number = parseInt(n1);
    console.log(calcSum(number));
});

function calcSum(number){
    let absNumber = Math.abs(number);
    let sum = 0;

    while(absNumber > 0){
        sum += absNumber % 10;
        absNumber = Number.parseInt(absNumber/10);
    }

    return sum;
}
