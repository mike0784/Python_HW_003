import random as rnd
n = int(input("Введите размер массива: "))
arr = []
for i in range(0, n):
    arr.append(rnd.randint(0, 100))

result = 0
for i in range(0, n):
    if i % 2 != 0:
        result = result + arr[i]

print(arr, "Ответ: " + str(result))