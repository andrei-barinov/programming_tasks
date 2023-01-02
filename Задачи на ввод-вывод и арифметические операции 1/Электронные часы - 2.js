//Электронные часы - 2
//Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
//
//С начала суток прошло n секунд. Выведите, что покажут часы.
//
//Входные данные
//
//Вводится целое число n.
//
//Выходные данные
//
//Выведите ответ на задачу, соблюдая требуемый формат.
//
//Sample Input:
//
//3602
//Sample Output:
//
//1:00:02

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (sec1) => {

    sec = +sec1 % (24 * 3600);

    var hour = getHour(sec);
    var min = getMin(sec);
    var secRem = getSec(sec);

    console.log(getResult(hour, min, secRem));
});

function getResult(h, m, s){

    let min = (m < 10) ? '0' + m : m;
    let sec = (s < 10) ? '0' + s : s;

    return h + ':' + min + ':' + sec;
}

function getSec(sec){
    return sec % 60;
}

function getMin(sec){
    return Number.parseInt((sec - 3600 * getHour(sec)) / 60);
}

function getHour(sec){
    return Number.parseInt(sec / 3600);
}