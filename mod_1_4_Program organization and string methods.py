from itertools import count

# Практическая работа по уроку "Организация программ и методы строк"

# 1 задание
my_string = input('Ваше имя и фамилия: ')
print(len(my_string))

# 2 Задание
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
first_symbol = my_string[0]
print('Первая буква: ', first_symbol)
the_last_character =  my_string[-1]
print('Последняя буква: ', the_last_character)