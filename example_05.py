import math
n = int(input("Введите число: "))

arr = [0, 1]
arr1 = []
for i in range(2, n + 1):
    arr.append(arr[i - 1] + arr[i - 2])
for i in range(1, n + 1):
    arr1.insert(0, (-1)**(i+1)*arr[i])

arr1 = arr1 + arr
print(arr1)