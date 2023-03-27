"""Даны натуральные числа k и s. 
Определите, сколько существует k-значных натуральных чисел, сумма цифр которых равна s. 
Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.

3 15 -> 69 # 
4 16 -> 564
2 3 -> 3
6, 40 ->10746 
"""

def find_numbers_func():
    k = int(input("Введите число k: "))
    s = int(input("Введите число s: "))
    min_num = 0                             # Минимальное значение
    max_num = 0                             # Максимальное возможное значение
    result_array = []                       # Массив для хранения результатов

    # Проверка суммы чисел двузначного числа
    if k == 2:
        min_num = 10
        max_num = 100
        while min_num < max_num:
            word_num = str(min_num)
            if int(word_num[0]) + int(word_num[1]) == s:
                result_array.append(min_num)
            min_num += 1

    # Проверка суммы чисел трехзначного числа
    if k == 3:
        min_num = 100
        max_num = 1000
        while min_num < max_num:
            word_num = str(min_num)
            if int(word_num[0]) + int(word_num[1]) + int(word_num[2]) == s:
                result_array.append(min_num)
            min_num += 1

    # Проверка суммы чисел четырехзначного числа
    if k == 4:
        min_num = 1000
        max_num = 10000
        while min_num < max_num:
            word_num = str(min_num)
            if int(word_num[0]) + int(word_num[1]) + int(word_num[2]) + int(word_num[3]) == s:
                result_array.append(min_num)
            min_num += 1

    # Проверка суммы чисел пятизначного числа
    if k == 4:
        min_num = 10000
        max_num = 100000
        while min_num < max_num:
            word_num = str(min_num)
            if int(word_num[0]) + int(word_num[1]) + int(word_num[2]) + int(word_num[3]) + int(word_num[4]) == s:
                result_array.append(min_num)
            min_num += 1
    
    # Проверка суммы чисел шестизначного числа
    if k == 4:
        min_num = 100000
        max_num = 1000000
        while min_num < max_num:
            word_num = str(min_num)
            if int(word_num[0]) + int(word_num[1]) + int(word_num[2]) + int(word_num[3]) + int(word_num[4]) + int(word_num[5]) == s:
                result_array.append(min_num)
            min_num += 1

    #print(result_array) # Вывод на экран всех вариантов
    return len(result_array)

# ======================== #
# Основной блок для запуска функции
print(find_numbers_func())
# ======================== #