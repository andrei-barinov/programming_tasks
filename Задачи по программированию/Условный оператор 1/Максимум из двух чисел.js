# Максимум из двух чисел
# Входные данные
#
# Даны два целых числа, каждое число записано в отдельной строке.
#
# Выходные данные
#
# Выведите наибольшее из данных чисел.
#
# Sample Input:
#
# 23
# 14
# Sample Output:
#
# 23

var stdin = process.openStdin();
stdin.addListener("data", function(d) {
    let data = d.toString().split('\n');
    let n = +data[0];
    let m = +data[1];
    getResult(n, m);
  });

function getResult(a, b){
    let result = a > b ? a : b;
    console.log(result);
}