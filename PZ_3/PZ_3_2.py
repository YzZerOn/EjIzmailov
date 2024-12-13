'''Вариант 10.
    Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.'''

def get_days_in_month(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return None  # Неверный номер месяца

while True:
    month = input("Введите номер месяца (1-12): ")
    try:
        month = int(month)
        days = get_days_in_month(month)
        if days is not None:
            print(f"Количество дней в месяце {month}: {days}")
            break
        else:
            print("Неверный номер месяца. Пожалуйста, введите число от 1 до 12.")
    except:
        print('Неверно введено число!')
