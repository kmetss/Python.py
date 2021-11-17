# однорядковий коментра
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
