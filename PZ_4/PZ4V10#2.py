"""Вариант 10.
Дано целое число N (> 1). Найти наибольшее целое число K, при котором
выполняется неравенство 3^K < N."""
while True:
    try:
        n = int(input("Введите целое число N (> 1): "))
        if n > 1:break
        raise ValueError
    except ValueError:
        print("Некорректный ввод.")

k = 0

for i in range(0,1000000):
    if 3**i < n:
        k += 1
    else:
        break

print("Наибольшее число K: ", k)
