cel = int(input("Введите целое число A"))
cel2 = int(input("Введите целое число B"))
if cel % 2 == 0 and cel2 % 2 != 0:
    print("Одно из чисел нечётное")
elif cel % 2 != 0 and cel2 % 2 == 0:
    print("Одно из чисел нечётное")
else:
    print("Оба числа чётные/нечётные")