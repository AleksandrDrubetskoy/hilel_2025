# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter, end="")

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
parameter = 4
banana = apples * parameter
print("")
print(apples, banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
#У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
#Скільки всього дерев посадили в саду?
"""
garden = 0
apples = 4
pears = apples + 5
plums = apples - 2
garden = apples + pears + plums
print(garden)

# task 08
"""
#До обіда температура повітря була на 5 градусів вище нуля.
#Після обіду температура опустилася на 10 градусів.
#Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning = 5
day = morning - 10
evening = day + 4
print(evening)

# task 09
"""
#Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
#1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
#Скількі сьогодні дітей у театральному гуртку?
"""
group = 0
boys = 24
girls = int(boys / 2)
boys = boys - 1
girls = girls - 2
group = boys + girls
print(group)

# task 10
"""
#Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
#а третя - як половина вартості першої та другої разом.
#Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
summ = book_1 + book_2 + book_3
print(summ)
