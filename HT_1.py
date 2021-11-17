# однорядковий коментар
'''
багаторядковий коментар


  1 .Write a script which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers.
'''
values = input ("Для відображення списків та кортежів, введіть ваші числа через кому:")
list = values.split (',')
tuple = tuple(list)
print('List:' , list)
print('Tuple:' , tuple)

'''
  2. Write a script to print out a set containing all the colours 
from color_list_1 which are not present in color_list_2.
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

'''
  3. Write a script to sum of the first n positive integers.
'''

n = int(input("Введіть число N: "))
sum = (n * (n + 1)) / 2
print('Сума перших натуральних чисел числа N дорівнює:' , sum)

'''
  4. Write a script to concatenate N strings.
'''

hello = 'Hello'
world = 'World'
    # 1 приклад
print(hello + ' ' + world)
    # 2 приклад
print(' '.join([hello, world]))
    # 3 приклад
print('%s %s' % (hello, world))
    # 4 приклад
print('{} {}'.format(hello, world))
    # 5 приклад
print(f'{hello} {world}')

'''
  5. Write a script to convert decimal to hexadecimal
'''

a = 30
b = 4
print(format(a, '02x'))
print(format(b, '02x'))

'''
  6. Write a script to check whether a specified value is contained in a group of values.
'''

def is_group_member(group_data, n):
   return n in group_data
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
