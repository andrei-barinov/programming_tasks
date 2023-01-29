arr = input().split(" ")

n = int(arr[0])
k = int(arr[1])
arrN = []

for i in range(n):
    arrN.append("I")

for i in range(k):
    arrK = input().split(" ")
    a = int(arrK[0])
    b = int(arrK[1])
    for i in range(len(arrN)):
        if i >= a-1 and i <= b-1:
            arrN[i] = "."
print("".join(arrN))