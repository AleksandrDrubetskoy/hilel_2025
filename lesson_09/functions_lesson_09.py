from collections import Counter

"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def computer_price (years, payment_per_month):
    '''
    This function returns payment for computer
    :param years: the number of years during which one has to pay for the computer
    :param payment_per_month: payment per month
    :return: total payment for computer
    '''
    months = int(12 * years)
    total_price = payment_per_month * months
    return total_price

"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    '''
    This function returns the index of first occurrence in string
    :param str1: first string
    :param str2: second string as search query
    :return: the index of first occurrence in string or -1 if there is no occurrence
    '''
    index = str1.find(str2)
    return index

"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers (numb_1, numb_2):
    '''
    This function calculates the sum of two numbers.
    :param numb_1: first number
    :param numb_2: second number
    :return: sum of numb_1 and numb_2
    '''
    total_sum = 0
    if isinstance(numb_1, int) and isinstance(numb_2, int):
        total_sum += numb_2 + numb_1
    else:
        total_sum = None
    return total_sum

def sum_doubles_only (list_with_doubles_val):
    list_counter_uniq_val = Counter(list_with_doubles_val)
    total_sum = 0
    for i, j in list_counter_uniq_val.items():
        if j % 2 == 0: # only for even doubles, like (a & a) or (a, a, a, a), etc. Doubles (a, a, a) is uneven.
            total_sum += int(i*j)
    return total_sum

"""  
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код,
який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
"""
def list_string (list_char):
    '''
    This function returns a list of string type variables
    :param list_char: any list with different type variables
    :return: list of string type variables
    '''
    lst2 = [i for i in list_char if isinstance(i, str)]
    return lst2