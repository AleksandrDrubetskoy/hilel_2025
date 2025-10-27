# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers (number):
    for i in range (0, number + 1, 2):
        yield i


ev_num = even_numbers(20)
for _ in range(5):
    try:
        print(next(ev_num))
    except StopIteration:
        print("StopIteration: Ітератор закінчився")

print("_"*44)

for _ in range(7):
    try:
        print(next(ev_num))
    except StopIteration:
        print("StopIteration: Ітератор закінчився")

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator(number):
    a, b = 0, 1
    while a <= number:
        yield a
        a, b = b, a + b


print("_"*44)

fib_gen = fibonacci_generator(20)
for _ in range (5):
    try:
        print (next(fib_gen))
    except StopIteration:
        print("StopIteration: Ітератор закінчився")

print("_"*44)

for _ in range (5):
    try:
        print (next(fib_gen))
    except StopIteration:
        print("StopIteration: Ітератор закінчився")

print("_"*44)

# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseNumbers:
    def __init__(self, list_numbers):
        self.list_numbers = list_numbers
        self.index_number = len(list_numbers)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_number == 0:
            raise StopIteration
        self.index_number -= 1
        return self.list_numbers[self.index_number]

rev_num = ReverseNumbers([1, 2, 5, 8, 12, 56])
for i in rev_num:
    print(i)

print("_"*44)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumbers:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        while self.number >= self.current:
            if self.current % 2 == 0:
                current_number = self.current
                self.current +=1
                return current_number
            self.current += 1
        raise StopIteration

range_numbers = EvenNumbers(19)
for i in range_numbers:
    print(i)

print("_"*44)

# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def arguments_and_result_log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function is {func.__name__}. Args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@arguments_and_result_log
def division(a, b):
    return a / b

division(12, 3)
print("_"*44)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def interception_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in function '{func.__name__}': {e}")
            return None
    return wrapper

@interception_exceptions
def division(a, b):
    return a / b

division(5, 0)