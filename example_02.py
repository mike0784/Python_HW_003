import random as rnd
import math
n = int(input("Введите размер массива: "))
arr = []
i = 0
while i < n:
    arr.append(rnd.randint(0, 100))
    i = i + 1

print(arr, end="  ")
for i in range(0, math.ceil(n / 2)):
    print(arr[i] * arr[n-1-i], end=" ")

print("")