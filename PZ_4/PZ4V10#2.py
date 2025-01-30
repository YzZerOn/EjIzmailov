"""Вариант 10.
Дано целое число N (> 1). Найти наибольшее целое число K, при котором
выполняется неравенство 3^K < N."""
def intcheck(x):
    while type(x) != int:
        try:
            x = int(x)
            if 1>x or x>12:
                raise ValueError
            return x
        except ValueError:
            print('Неправильный ввод месяца!')
            x = input('Повторите попытку: ')

mes = intcheck(input("Введите номер месяца: "))

if mes in (1, 3, 5, 7, 8, 10, 12):
    print("Дней в месяце - 31")
elif mes in (4, 6, 9, 11):
    print("Дней в месяце - 30")
elif mes == 2:
    print("Дней в месяце - 28")
