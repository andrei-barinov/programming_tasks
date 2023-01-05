# Ноль или не ноль
# Проверьте, есть ли среди данных N чисел нули.
#
# Входные данные
#
# Вводится число N, а затем N чисел.
#
# Выходные данные
#
# Выведите YES, если среди введенных чисел есть хотя бы один нуль, или NO в противном случае.
#
# Sample Input:
#
# 3
# 1
# 0
# 2
# Sample Output:
#
# YES

n = int(input());

sum = 0;

for i in range(0, n):
    a = int(input());
    if a == 0:
        sum +=1;
if sum > 0:
    print('YES');
else:
    print('NO');