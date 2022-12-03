import random as rnd
import math
n = int(input("Введите размер массива: "))
arr = []
for i in range(0, n):
    arr.append(rnd.uniform(0, 100))

minVar = arr[0] - math.trunc(arr[0])
maxVar = arr[0] - math.trunc(arr[0])

for item in arr:
    a = item - math.trunc(item)
    if a < minVar:
        minVar = a
    elif a > maxVar:
        maxVar = a
print(arr)
print("Ответ: " + str(maxVar - minVar))