def find_password(n):
#Список для хранения пар
    pairs = []

#Перебираем числа от 1 до 20
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) % n == 0:
                pairs.append((i, j))

#Составляем пароль из пар
    password = ''.join(f"{a}{b}" for a, b in pairs)
    return password

#Примеры вызова функции для чисел от 3 до 20
for n in range(3, 21):
    print(f"{n} - {find_password(n)}")