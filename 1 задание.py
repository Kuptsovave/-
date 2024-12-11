d = int(input())  # ПОКАЗАТЕЛЬ КАЧ-ВА МАТЕРИАЛА
x = int(input())  # КОЛ-ВО РАБОЧИХ ДНЕЙ
a = (365 - 75 / d ** 3) / (3 * d ** 2 - d) * 5  # ПРОИЗВОДИТЕЛЬНОСТЬ 1-ОГО РАБОЧЕГО
b = (412 - 125 / d ** 3) / (2 * d ** 2 - d) * 4  # ПРОИЗВОДИТЕЛЬНОСТЬ 2-ОГО
count_a = 0
count_b = 0
for day in range(x):
    count_a += a
    count_b += b
res = int(count_a) + int(count_b)
print(res)
