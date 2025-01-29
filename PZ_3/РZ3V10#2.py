mes = int(input("Введите номер месяца "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Дней в месяце - 31")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Дней в месяце - 30")
elif mes == 2:
    print("Дней в месяце - 28")
