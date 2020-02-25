
'''
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

number = 13195
numbers = [i for i in range(1, number)]
devisors = []
for i in range(1, len(numbers)):
    if number % i == 0:
        devisors.append(i)
print(devisors)
simple_devisors= []
for n in devisors:
    i = 2
    j = 0 #флаг
    while i**2 <= n and j !=1:
        if n%i == 0:
            j = 1
        i+=1
    if j == 1:
        pass
    else:
        simple_devisors.append(n)

print(simple_devisors)
print(max(simple_devisors))
