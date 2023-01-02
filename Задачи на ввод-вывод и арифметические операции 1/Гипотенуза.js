# Гипотенуза

# Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
#
# Входные данные
#
# В двух строках вводятся два числа (числа целые, положительные, не превышают 1000).
#
# Выходные данные
#
# Выведите ответ на задачу в виде целого числа

# Sample Input:
# 6
# 8
#
# Sample Output:
# 10

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (a1) => {
    r1.on('line', (b1) => {

        a = parseInt(a1);
        b = parseInt(b1);

        result = calcHypot(a, b);

        console.log(result);

    });
});

function calcHypot(a, b){
    return Number.parseInt(Math.sqrt((a * a + b * b)));
}