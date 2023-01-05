# Нули
# Входные данные
#
# Вводится число N, а затем N чисел.
#
# Выходные данные
#
# Подсчитайте и выведите, сколько среди данных N чисел нулей.
#
# Sample Input:
#
# 3
# 1
# 2
# 3
# Sample Output:
#
# 0

n = int(input());

sum = 0;

for i in range(0, n):
    a = int(input());
    if a == 0:
        sum += 1;

print(sum);