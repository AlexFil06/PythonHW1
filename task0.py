# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


num = int(input('Введите трехзначное число число -> '))
if (100 <= num) and (num <= 999):
    print(num, end=' -> ')   #эту фишку подсмотрел в интеренете, остальной код правда мой) 
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    print(sum)

else:
    print('Число не трехзначное')
