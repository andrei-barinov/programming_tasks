# Послезавтра
# По заданной дате требуется определить, какое число будет послезавтра.
#
# Напомним, что год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
#
# Входные данные
#
# Дано число, месяц и год (год  – число в промежутке от 1 до 10000).
#
# Выходные данные
#
# Требуется вывести, какое число будет послезавтра, в формате входных данных.
#
# Sample Input:
#
# 1 8 2009
# Sample Output:
#
# 3 8 2009

n = input().split(" ");

day = int(n[0]);
m = int(n[1]);
year = int(n[2]);

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if day == 30:
            result_day = 1;
            if m == 12:
                result_m == 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        elif day == 31:
            result_day = 2;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if day == 29:
            result_day = 1;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        elif day == 30:
            result_day = 2;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
    elif m == 2:
        if day == 28:
            result_day = 1;
            result_m = m + 1;
            result_year = year;
        elif day == 29:
            result_day = 2;
            result_m = m + 1;
            result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if day == 30:
            result_day = 1;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m == m + 1;
                result_year == year;
        elif day == 31:
            result_day = 2;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if day == 29:
            result_day = 1;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        elif day == 30:
            result_day = 2;
            if m == 12:
                result_m = 1;
                result_year = year + 1;
            else:
                result_m = m + 1;
                result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
    elif m == 2:
        if day == 27:
            result_day = 1;
            result_m = m + 1;
            result_year = year;
        elif day == 28:
            result_day = 2;
            result_m = m + 1;
            result_year = year;
        else:
            result_day = day + 2;
            result_m = m;
            result_year = year;
print(result_day, result_m, result_year, sep = " ");