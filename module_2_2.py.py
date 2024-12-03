first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция
if first == second == third:
    # Если все числа равны между собой
    print(3)
elif first == second or second == third or first == third:
    # Если хотя бы два из трех чисел равны между собой
    print(2)
else:
    # Если равных чисел среди трех вообще нет
    print(0)