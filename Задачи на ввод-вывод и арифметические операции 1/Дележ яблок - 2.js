//Дележ яблок - 2
//N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок останется в корзинке?
//
//Входные данные
//
//Программа получает на вход числа N и K.
//
//Выходные данные
//
//Программа должна вывести искомое количество яблок.
//
//Sample Input:
//
//5
//21
//Sample Output:
//
//1

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    r1.on('line', (k1) => {
        n = parseInt(n1);
        k = parseInt(k1);
        console.log(k1 % n1);
    });
});