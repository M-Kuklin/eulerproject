
'''Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.'''
fibbon = [i for i in range(1, 11)]
for i in range(0, len(fibbon)):
    if i == 7:
        break
    else:
        fibbon[i + 3] = fibbon[i + 2] + fibbon[i + 1]
        #print(i)
print(fibbon)

sum = 0
for i in fibbon:
     if i % 2 == 0:
          sum += i
print(sum)

