# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множеста: "))
m = int(input("Введите кол-во элементов второго множества: "))

first = []
second = []

for i in range(n):
    first.append(int(input("Введите элемент первого множества: ")))

for i in range(m):
    second.append(int(input('Введите элемент для второго множества: ')))


c = set(first) & set(second)
print(c)





# Задача 24:

n = int(input("Введите количество кустов: "))
a = []

for i in range(n):
    a.append(i+1)

c = int(input(f"Введите номер куста для отправки собирающего модуля"
              f" (всего кустов {n}): "))
for i in range(n):
    result = 0
    if c == n:
        result = n-1 + n + 1
        break
    if c == 1:
        result = n + c + c+1
        break
    elif c == i:
        result = c-1 + c + c+1
    i += 1

print(result)


