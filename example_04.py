n = int(input("Введите число: "))

text = ""

while n > 0:
    text = str(n % 2) + text
    n = n // 2

print("Ответ: " + text)