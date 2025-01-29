while True:
    cel = int(input("Введите целое число N (N>1) "))
    if cel > 1:
        break
mass = []
for i in range(0,50):
    if 3**i < cel:
        mass.append(i)
print("Наибольшее число K: ", max(mass))