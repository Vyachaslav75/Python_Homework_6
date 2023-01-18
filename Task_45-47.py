

#45  Сумма чисел списка стоящих на нечетной позиции
a = [x for x in range(15)]
print(f'Список {a}', end='\n\n')
print('Сумма эл-тов на нечетных позициях = ', end='')
print(sum([v for i, v in enumerate(a) if i % 2 == 1]), end='\n\n')

#46
print('Произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)')
a1 = [v for i, v in enumerate(a) if i < len(a)//2]
a.reverse()
a2 = [v for i, v in enumerate(a) if i < len(a)//2]
print(list(map(lambda x, y: x*y, a1, a2)), end='\n\n')

#47 список из N членов последовательности  
# (каждый член больше предыдущего в три раза, знак чередуется)
print('Формирует список из N членов последовательности')
print('каждый член больше предыдущего в три раза, знак чередуется')
n=int(input('Введите N= '))
list1 = [(3**x)*((-1)**x) for x in range(n)]
print(f'N={n}: {list1}')
