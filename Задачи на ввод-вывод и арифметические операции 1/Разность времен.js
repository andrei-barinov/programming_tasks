//Разность времен
//Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени.
//
//Входные данные
//
//Программа на вход получает три целых числа — часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.
//
//Выходные данные
//
//Выведите число секунд между этими моментами времени.
//
//Sample Input:
//
//1
//1
//1
//2
//2
//2
//Sample Output:
//
//3661

const readline = require('readline');

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

r1.once('line', (h1) => {
    r1.once('line', (m1) => {
        r1.once('line', (s1) => {
           r1.on('line', (h2) => {
                r1.on('line', (m2) => {
                    r1.on('line', (s2) => {
                        h_1 = +h1;
                        m_1 = +m1;
                        s_1 = +s1;

                        h_2 = +h2;
                        m_2 = +m2;
                        s_2 = +s2;

                        console.log(getResult(h_1, m_1, s_1, h_2, m_2, s_2));
                    });
                });
           });
        });
    });
});

function getResult(h1, m1, s1, h2, m2, s2){
    let t1 = 3600 * h1 + 60 * m1 + s1;
    let t2 = 3600 * h2 + 60 * m2 + s2;

    return t2 - t1;
}