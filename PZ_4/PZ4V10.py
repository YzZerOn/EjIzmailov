"""Вариант 10.
Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2"""
while True:
    try:
        n = int(input("Введите целое число N (> 0): "))
        if n > 0:
            break
        raise ValueError
    except ValueError:
        print("Некорректный ввод.")

sum = 0
for i in range(0,1000000):
    sum += (n+i)**2
    if (n+i) == 2*n:
        break
print("Сумма: ", sum)
