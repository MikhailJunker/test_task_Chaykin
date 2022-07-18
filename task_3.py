from random import choice
from random import randint

def quick_sort(arr):
   if len(arr) <= 1:
       return arr
   else:
       reference_element = choice(arr)
       left_part = []
       equal_nums = []
       right_part = []
       for num in arr:
           if num < reference_element:
               left_part.append(num)
           elif num > reference_element:
               right_part.append(num)
           else:
               equal_nums.append(num)
       return quick_sort(left_part) + equal_nums + quick_sort(right_part)

# len_arr = randint(1, 1000)
# arr = [randint(-10000, 10000) for i in range(len_arr)]
# print(quick_sort(arr))



######################################################################
#
# Быстрая сортировка:
#   +:
#     1) Асимптотика: в среднем и лучшем случае - O(n*logn), наихудший случай - O(n^2) - достигается при неудачном
#     выборе опорного элемента на каждой итерации сортировки.
#
#   -:
#     1) Быстрая сортировка показывает хорошие временные результаты на полностью случайном массиве данных, на
#        частично отсортированном массиве данных, а также на отсортированном массиве данных с небольшим
#        числом перестановок двух случайных чисел
#
######################################################################