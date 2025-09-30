a={}

while True:
    name = input("Ім'я студента або стоп")
    if name == "stop":
        break
    age = int(input("Оцінка"))
    a[name] = age

print('Список студентів')
for name, age in a.items():#item повертаэ всі значення кортежу
    print(name,":", age)

avg=sum(a.values()) / len(a) #len Кількість елементів (оцінок)
excellent = [n for n, g in a.items() if 10 <= g <= 12]
good = [n for n, g in a.items() if 7 <= g <= 9]
bad = [n for n, g in a.items() if 4 <= g <= 6]
failed = [n for n, g in a.items() if 1 <= g <= 3]

print("Відмінники:", excellent)
print("Хорошисти:", good)
print("Відстаючі:", bad)
print("Не здали:", failed)




