weight = int(input("Введите вес очных матчей: "))
lastweight = int(input("Вес последних матчей: "))

xc = input("Тоталы очных матчей(через запятую): ")
xa = input("Тоталы 1-ой команды(через запятую): ")
xb = input("Тоталы 2-ой команды(через запятую): ")

xc = str.split(xc, ",")
xa = str.split(xa, ",")
xb = str.split(xb, ",")

print("---------")
print("Проверьте правильность введёных данных: ")
print("Тоталы очных: "+str(xc))
print("Тоталы 1-ой команды: "+str(xa))
print("Тоталы 2-ой команды: "+str(xb))


def summ(arr):
    kol = 0
    tempweight = lastweight
    summ = 0
    for i in arr:
        summ = summ + (float(i) * tempweight)
        kol = kol + tempweight
        tempweight = max(1, tempweight - 1)
    return summ / kol


print("\n")
print("Средний тотал(ставьте меньше): "+str((weight*summ(xc)+summ(xa)+summ(xb))/(2+weight)))
