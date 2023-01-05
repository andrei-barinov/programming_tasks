# Сумма ста
# Вычислите сумму данных 100 натуральных чисел.
#
# Входные данные
#
# Вводятся 100 чисел, сумму которых необходимо посчитать.
#
# Выходные данные
#
# Программа должна вывести единственное число - полученную сумму.
#
# Sample Input:
#
# 206 443 825 103 336 98 473 134 432 413 119 71 726 837 92 298 141 582 391 232 76 652 881 17 985 4 289 255 80 12 569 308 410 217 846 323 591 925 665 363 365 857 200 162 340 58 411 745 478 25 158 662 26 575 504 51 910 803 127 987 913 489 674 433 531 619 683 197 26 507 432 144 448 746 66 190 737 127 615 948 340 317 689 731 455 695 284 471 717 274 195 175 48 130 211 186 877 716 228 277
# Sample Output:
#
# 41405

str = input();
numbers = str.split(' ');

sum = 0;

for n in range(0, len(numbers)):
    sum += int(numbers[n]);

print(sum);