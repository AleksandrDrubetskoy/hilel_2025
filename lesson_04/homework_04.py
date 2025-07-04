adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"Task_01")
print(adwentures_of_tom_sawer)
print("")
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"Task_02")
print(adwentures_of_tom_sawer)
print("")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(f"Task_03")
print(adwentures_of_tom_sawer)
print("")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f"Task_04")
print(f"The number of letters \'h\' in line is {adwentures_of_tom_sawer.count("h")}")
print("")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list = adwentures_of_tom_sawer.split()
sum = 0
for i in list:
    if i.istitle() == True:
        sum = sum + 1
print(f"Task_05")
print(f"The number of words that begin with capital letter is {sum}")
print("")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print(f"Task_06")
print(f"Position for second occurance of word \"Tom\" is {adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)}")
print("")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(f"Task_07")
print(adwentures_of_tom_sawer_sentences)
print("")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"Task_08")
string = None
num = 0
for i in adwentures_of_tom_sawer_sentences:
    num = num + 1
    if num == 4:
        string = i
        break
print(string)
print(string.lower())
print("")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
sum = 0
for i in adwentures_of_tom_sawer_sentences:
    j = i.startswith("By the time")
    if j == True:
        sum = sum + 1
print(f"Task_09")
print(f"The number of sentences starts from \"By the time\" is {sum}")
print("")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
string_fin = adwentures_of_tom_sawer_sentences[-1]
print(f"Task_10")
print(f"The number of words in last sentence is {string_fin.count(" ") + 1}")
print("")
