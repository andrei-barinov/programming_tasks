//Дележ яблок - 1
//
//N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
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
//4

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (n1) => {
    r1.on('line', (k1) => {
        n = parseInt(n1);
        k = parseInt(k1);
        c = Number.parseInt(k / n);
        console.log(c);
    });
});