alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print (alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


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
black_sea_square = 436 402
azov_sea_square = 37 800
task04_str = f"Black Sea square is {black_sea_square} km^2, but Azov sea square is {azov_sea_square} km^2.\n What is Black Sea square and Azov Sea in sum?"
print(task04_str)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375 291
first_and_second_storages = 250 449
second_and_third_storages = 222 950

task05_str = (f"The chain of supermarkets has 3 storages, where totaly is placed {total_goods} of goods./n on the first and the second storages there are placed {first_and_second_storages} of goods./n"
              f"On the second and third storages there are placed {second_and_third_storages} of goods./n"
              f"How many goods is placed on each storage?")
print(task05_str)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payments = 1179
task06_str = (f"Mykhailo together with his parents decided to buy PC, using the service 'Payment by installments'.\n"
              f"It is known that they must to pay {month_payments} per month during the one year and a half.\n"
              f"What is the cost of the PC? ")
print(task06_str)


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

task07_str = (f"Find the remainder of the division of numbers:\n"
              f"a) {a}\t d) {d} \n"
              f"b) {b}\t e) {e} \n"
              f"c) {c}\t f) {f} \n")
print(task07_str)

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
pizza_huge_amount = 4
pizza_huge_price = 274
pizza_middle_amount = 2
pizza_middle_price = 218
juice_amount = 4
juice_price = 35
cake_amount = 1
cake_price = 350
water_amount = 3
water_price = 21

task08_str = (f"Irynka during the preparations to here birthday preparations, prepared the list of thing she needs to order.\n"
              f"Calculate how much money she needs to make her order.n\"
              f"Pizza huge\t {pizza_huge_amount}\t {pizza_huge_price}\n"
              f"Pizza middle\t {pizza_middle_amount}\t {pizza_middle_price}\n"
              f"Juice\t {juice_amount}\t {juice_price}\n"
              f"Cake\t {cake_amount}\t {cake_price}\n"
              f"Water\t {water_amount}\t {water_price}\n")
print(task08_str)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photo_per_page = 8
task09_str = (f"Ihor is doing photography. He decided to collect his all {all_photos} photos\n"
              f"and glue them into album. ther ecan be at most {photo_per_page} photos on one page.\n"
              f"How many pages it will take to Ihor to glue all the photos?")

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
distance = 1600
gas_pers_100_km = 9
tank_capacity = 48

task10_str = (f"The family is going to make the trip by auto form Kharkiv to Budapesht. "
              f"The distance between these cities is {distance} km.\n"
              f"It is known that fow every 100 km they need {gas_pers_100_km} l of the gas"
              f"The tank capacity is {tank_capacity}.\n"
              f"1) How much of the gas is needed for such trip?"
              f"2) How many times the family would need attend gas station during the trip, if they filled up the full tank every time ?"
               )
print(task10_str)