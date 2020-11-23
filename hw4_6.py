'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
 создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
 '''
from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


my_count_func(start_number=int(input("введите стартовое число: ")), stop_number=int(input("введите конечное число: ")))
