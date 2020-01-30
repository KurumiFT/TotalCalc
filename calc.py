wins = input("Введите коэффициенты на победы первой и второй команды(через запятую) : ").split(",")
weight = int(input("Введите вес очных матчей: "))
lastweight = int(input("Вес последних матчей: "))

xc = input("Тоталы очных матчей(через запятую): ").split(",")
xa = input("Тоталы 1-ой команды(через запятую): ").split(",")
xb = input("Тоталы 2-ой команды(через запятую): ").split(",")

print("---------")
print("Проверьте правильность введёных данных: ")
print("Тоталы очных: "+str(xc))
print("Тоталы 1-ой команды: "+str(xa))
print("Тоталы 2-ой команды: "+str(xb))

def max_arr(arr):
    max = 0
    for i in xc:
        if int(i) > max:
            max = int(i)
    return max

def min_arr(arr):
    min = 1000
    for i in xc:
        if int(i) < min:
            min = int(i)
    return min

def summ(arr):
    kol = 0
    tempweight = lastweight
    summ = 0
    for i in arr:
        summ = summ + (float(i) * tempweight)
        kol = kol + tempweight
        tempweight = max(1, tempweight - 1)
    return summ / kol

normal = (weight*summ(xc)+summ(xa)+summ(xb))/(2+weight)

print("\n")
print("Средний тотал(не ориентируйтесь на него): "+str(normal))
print("---------------------------------------")

if (max(float(wins[0]),float(wins[1])) - min(float(wins[0]),float(wins[1])) <= 1):
    print("Рекомендуем ставить на Тотал {Total}М".format(Total=(normal+max_arr(xc))/2))
else:
    print("Рекомендуем ставить на Тотал {Total}Б".format(Total=((normal+min_arr(xc))/2)))
