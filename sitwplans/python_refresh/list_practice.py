


my_list = ['spinach', 'egg', 'tomato']
list_to_string = ', '.join(my_list)

print(list_to_string)
print(my_list)

print('\n'.join(my_list))
print(str(my_list).strip('[]'))
print(str(my_list)[1:-1])

num_list = [1, 2, 3, 4, 5]

print(', '.join(map(str, num_list)))