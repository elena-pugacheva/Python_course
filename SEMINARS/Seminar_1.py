# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# **Input:**

# n = 700

# m = 750

# 1 решение.
# n = int(input('Сколько машина проезжает за день: '))

# m = int(input('Введите длину маршрута: '))

# print(f"Нужно {(m//n)+bool(m%n)} дней")

# 2 решение.
# n = int(input())
# m = int(input())
# # 100
# # 200
# # 200 + 100 - 1 = 299  // 100 = 2

# s = (m + n - 1) // n
# print(s)


# 2 ex
# i = int(input('Введите номер вагона по счету: '))
# j = int(input('Введите номер, указанный на вагоне: '))
# if i==j:
#     print("Нужна дополнительная информация") # не известно с начала или с конца идет счет, если с начала, то неизвестно сколько вагонов дальше
# else:
#     n = j + i-1
#     print(n)


# 3 ex
# klass_1 = int(input("Количество учеников в 1 классе: "))
# klass_2 = int(input("Количество учеников во 2 классе: "))
# klass_3 = int(input("Количество учеников в 3 классе: "))

# print(f"Нужно {(klass_1+1)//2+(klass_2+1)//2+(klass_3+1)//2} парт")


# 4 ex.
# year = int(input("Введите год: "))
# if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#     print("YES")
# else:
#     print("NO")