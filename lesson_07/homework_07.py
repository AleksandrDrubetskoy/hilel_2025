# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    '''
    This function returns the multiplication of two numbers until their product is greater than 25
    :param number: the number
    :return: several strings with product of the number and multiplier
    '''
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
print("_"*40)
print("Task 1")
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
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
print("_"*40)
print("Task 2")
print(sum_two_numbers(10, 12))
print(sum_two_numbers(1, "Sasha"))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean (*numbers):
    '''
    This function calculates the arithmetic mean of a list of numbers
    :param numbers: list of numbers
    :return: arithmetic mean of a list of numbers
    '''
    total_list_numbers = [*numbers]
    amount_int = 0
    for i in total_list_numbers:
        if isinstance(i, int):
            amount_int += 1
    total_list_int = []
    if amount_int > 0:
        total_list_int = [i for i in total_list_numbers if isinstance(i, int)]
    total_sum = 0
    for i in total_list_int:
        total_sum += i
    if amount_int != 0:
        arithm_mean = total_sum/len(total_list_int)
    else:
        arithm_mean = None
    return arithm_mean
print("_"*40)
print("Task 3")
print(arithmetic_mean(5, 6, 9, 12, "Sasha", 3, 6, "David"))
print(arithmetic_mean("Sasha", "David"))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_stroke (string_in):
    '''
    This function reverse a string
    :param string_in: string
    :return: reverse string
    '''
    if isinstance(string_in, str):
        reverse = string_in[::-1]
    else:
        reverse = None
    return reverse
print("_"*40)
print("Task 4")
print (reverse_stroke("Sasha David"))
print(reverse_stroke(5))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word (*words):
    '''
    This function returns the longest word from list of words
    :param words: list of words
    :return: the longest words
    '''
    list_of_words = [*words]
    longest_word_i = ""
    len_word = 0
    for i in list_of_words:
        if len(i) > len_word:
            len_word = len(i)
            longest_word_i = i
    return longest_word_i
print("_"*40)
print("Task 5")
print (longest_word("David", "Sasha", "Oleksandr", "Samanta", "Vasilisa"))

# task 6
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
print("_"*40)
print("Task 6")

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def album_pages (photo_amount, photo_per_page):
    '''
    This function returns the number of pages for photo album
    :param photo_amount: the number of photos
    :param photo_per_page: the number of pages for photo album
    :return:
    '''
    complete_pages = photo_amount // photo_per_page
    incomplete_page = photo_amount % photo_per_page
    if incomplete_page > 0:
        incomplete_page = 1
    return complete_pages + incomplete_page

print("_"*40)
print("Task 7")
print(album_pages(232, 8))

# task 8
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

print("_"*40)
print("Task 8")
print(f"Total payment: {computer_price(1.5, 1179)} grn")

# task 9
"""
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. 
Строку отримати за допомогою функції input()
"""
def total_uniq_char (string_inp):
    '''
    This function returns the number of unique characters in the input string
    :param string_inp: the input string
    :return: True if the number of unique characters in the input string is more than 10 or False if the number is <=10
    '''
    new_set = set(string_inp)
    return len(new_set) > 10

print("_"*40)
print("Task 9")
print(total_uniq_char(input("Enter txt: ")))

# task 10
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

print("_"*40)
print("Task 10")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(list_string(lst1))
