weight = int(input("Введите вес очных матчей: "))

xc = input("Тоталы очных матчей(через запятую): ")
xa = input("Тоталы 1-ой команды(через запятую): ")
xb = input("Тоталы 2-ой команды(через запятую): ")

xc = str.split(xc,",")
xa = str.split(xa,",")
xb = str.split(xb,",")

print(xc)
print(xa)
print(xb)

def summ(arr):
    summ = 0
    for i in arr:
        summ = summ + float(i)
    return  summ

print(((weight*(summ(xc)/len(xc)))+(summ(xa)/len(xa))+(summ(xb)/len(xb)))/(3+weight))
