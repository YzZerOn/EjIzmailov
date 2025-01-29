while True:
    cel = int(input("Введите N>0: "))
    if cel > 0:
        break
sum = 0
for i in range(0,1000000):
    sum += (cel+i)**2
    if (cel+i) == 2*cel:
        break
print(sum)