//МКАД
//Длина Московской кольцевой автомобильной дороги — 109 километров. Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
//
//Входные данные
//
//Программа получает на вход значения v и t. Если v>0, то Вася движется в положительном направлении по МКАД, если же значение v<0, то в отрицательном.
//
//Выходные данные
//
//Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.
//
//Sample Input 1:
//
//60
//2
//Sample Output 1:
//
//11
//Sample Input 2:
//
//-1
//1
//Sample Output 2:
//
//108

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.on('line', (v1) => {
    r1.on('line', (t1) => {
        v = parseInt(v1);
        t = parseInt(t1);
        console.log(calcDistanse(v, t));
    });
});

function calcDistanse(v, t){
    const l = 109;
    var s = v * t;

    if(v >=0){
        result = (s <= l) ? s : s % l;
    } else{
        var absS = Math.abs(s);
        result = (absS <= l) ? (l - absS) : (109 - absS % l);
    }

    return result;
}