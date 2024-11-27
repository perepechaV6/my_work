my_dict = {'Lidiya': 2002, 'ilya': 1999, 'Liza': 2004}
print(f"Dict: {my_dict}")
existing_key = 'Liza'
print(f"Existing value: {my_dict.get(existing_key)}")
non_existing_key = 'Ivan'
print(f"Not existing value: {my_dict.get(non_existing_key)}")
my_dict['Uliya'] = 2000
my_dict['Nikolay'] = 1915
key_to_delete = 'ilya'
deleted_value = my_dict.pop(key_to_delete, None)
print(f"Deleted value: {deleted_value}")
print(f"Modified dictionary: {my_dict}")
my_set = {1, 'Помидор', 43, 1, 'Помидор'}
print(f"Set: {my_set}")
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(f"Modified set: {my_set}")