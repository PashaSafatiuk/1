# Створюємо список із 10 int та 10 str
list = [5, 2, 9, 8, 1, 4, 6, 3, 7, 10,
           "banana", "apple", "cherry", "grape", "kiwi",
           "pear", "orange", "plum", "melon", "lemon"]


ints = sorted([x for x in list if isinstance(x, int)])  # Перебирає всі значення ліста потім бере значення інт і заносить в змінну інтс
strings = sorted([x for x in list if isinstance(x, str)])
x2 = [x for x in ints if x % 2 == 0]
up = [x.upper() for x in strings]

print("Головний відсортований список:", ints + strings)
print("Список чисел, кратних 2:", x2)
print("Список строк у верхньому регістрі:", up)
