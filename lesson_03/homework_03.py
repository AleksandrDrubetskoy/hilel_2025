
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where ——" said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'''
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_Black_sea = 436402
square_Azov_sea = 37800
total = square_Black_sea + square_Azov_sea
print("Task_04")
print(f"Total square of two seas: {total} km2")
print(' ')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
products = 375291
prod_1 = 250440
prod_2 = 222950
storage_3 = products - prod_1
storage_1 = products - prod_2
storage_2 = products - (storage_3 + storage_1)
print("Task_05")
print(f"Storage №1: {storage_1} products, Storage #2: {storage_2} products, Storage #3: {storage_3} products")
print(' ')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
years = 1.5
months = int(12 * years)
payment_per_month = 1179
total = payment_per_month * months
print("Task_06")
print(f"Total payment: {total} grn")
print(' ')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Task_07")
print(8019 % 8, 9907 % 9, 2789 % 5, 7248 % 6, 7128 % 5, 19224 % 9, sep="\n")
print(' ')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_l_amount = 4
pizza_l_price = 274
pizza_m_amount = 2
pizza_m_price = 218
juice_amount = 4
juice_price = 35
cake_amount = 1
cake_price = 350
water_amount = 3
water_price = 21
total = pizza_l_amount * pizza_l_price + pizza_m_price * pizza_m_amount + juice_price * juice_amount + cake_price * cake_amount + water_price * water_amount
print("Task_08")
print(f"Irina needs: {total} hrn")
print(
    f"Including large pizza: {pizza_l_amount * pizza_l_price} hrn, "
    f"middle pizza {pizza_m_price * pizza_m_amount} hrn, juice: {juice_price * juice_amount} hrn,"
    f" cake: {cake_amount * cake_price} hrn, water: {water_price * water_amount} hrn")
print(' ')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pfotos = 232
photos_per_page = 8
complete_pages = pfotos // photos_per_page
incomplete_page = pfotos % photos_per_page
album = complete_pages + incomplete_page
print("Task_09")
print(f"Ihor needs {album} pages")
print(' ')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
length_total = 1600
length_100 = 100
oil_amount_per_100_km = 9
oil_volume = 48
oil_total = length_total / length_100 * oil_amount_per_100_km
refuel_1 = oil_total // oil_volume
refuel_2 = 0
if oil_total % oil_volume > 0:
    refuel_2 = 1
refuel_total = refuel_1 + refuel_2
print("Task_10")
print(f"Oil: {oil_total}l, number of fuel fills: {int(refuel_total)}")
