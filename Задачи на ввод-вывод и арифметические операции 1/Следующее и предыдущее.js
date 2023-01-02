//Следующее и предыдущее
//Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере. Пробелы, знаки препинания, заглавные и строчные буквы важны!
//
//Входные данные
//
//Вводится целое число, по модулю не превосходящее 10000.
//
//Выходные данные
//
//Выведите сначала фразу "The next number for the number ", затем введенное число, затем слово " is ", окруженное пробелами, затем формулу для следующего за введенным числа, наконец, знак точки без пробела. Аналогично в следующей строке для предыдущего числа.
//
//Sample Input:
//
//179
//Sample Output:
//
//The next number for the number 179 is 180.
//The previous number for the number 179 is 178.

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (a1) => {
    a = parseInt(a1);
    b = a;
    console.log('The next number for the number ' + a + ' is ' + ++a +'.');
    console.log('The previous number for the number ' + b + ' is ' + --b +'.')
});
