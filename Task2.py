# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input("Введите натуральное неотрицательное число больше 1, но не больше 100 тысяч: "))
while (a > 100000) or (a < 0) or (a in range(0, 2)):
    print("Вы ввели некорректное значение")
    a = int(input("Введите еще раз натуральное неотрицательное число больше 1, не больше 100 тысяч: "))
# print(a)
b = 2
d = 0
e = 0
for i in range(2, a):
    c = a // b
    # print(c)
    d = c * b
    # print(d)
    e = a - d
    if d == a:
        print('Число является составным')
        break
    else:
        b = b + 1
if e == 1:
    print('Число является простым')
if a == 2:
    print('Число является простым')