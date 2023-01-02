//Стоимость покупки
//Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
//
//Входные данные
//
//Программа получает на вход три числа: a, b, n.
//
//Выходные данные
//
//Программа должна вывести два числа: стоимость покупки в рублях и копейках.
//
//Sample Input:
//
//10
//15
//2
//Sample Output:
//
//20 30

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (a1) => {
    r1.on('line', (b1) => {
        r1.on('line', (n1) => {
            a = parseInt(a1);
            b = parseInt(b1);
            n = parseInt(n1);
            console.log(getResult(a, b, n));
        });
    });
});

function getResult(a, b, n){
    let pricePerCake = a * 100 + b;
    let priceAllCakes = n * pricePerCake;

    return Number.parseInt(priceAllCakes / 100) + ' ' + priceAllCakes % 100;
}