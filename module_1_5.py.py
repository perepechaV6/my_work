immutable_var = tuple([1, 2, 'a', 'b'])
print(f"Immutable tuple: {immutable_var}")
try:
    immutable_var[0] = 10
except TypeError as e:
    print(f"Ошибка: {e}. Кортежи являются неизменяемыми объектами, поэтому их элементы нельзя изменить.")
mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print(f"Mutable list: {mutable_list}")
